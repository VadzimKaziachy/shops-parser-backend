from django import forms
from typing import NoReturn
from django.conf import settings
from scrapyd_api import ScrapydAPI
from service_objects.services import Service

from .models import (
    ScrapyModel,
    ProductModel,
    CategoryModel,
    ParserProductModel,
)


class HandlerProductsService(Service):
    """
    Class processes data from the store.

    Fields:
        1) id - an object of type InteriorModel;
    """

    id = forms.IntegerField()

    def process(self) -> NoReturn:
        parser_products = list()
        scrapy_objects = ScrapyModel.objects.filter(id=self.cleaned_data['id'])

        if scrapy_objects.exists():
            scrapy_object = scrapy_objects.first()

            for new_product in scrapy_object.data:
                product, is_created = ProductModel.objects.get_or_create(
                    name=new_product.get('name'),
                    code=new_product.get('code'),
                    category=scrapy_object.category,
                    defaults={'code': new_product.get('code')}
                )

                parser_products.append(ParserProductModel(product=product, price=float(new_product.get('price'))))

            ParserProductModel.objects.bulk_create(parser_products)

            scrapy_object.delete()


class ParsingService(Service):
    """
    Class launches a parser from each category.
    """

    def process(self) -> NoReturn:
        categories = CategoryModel.objects.all()
        scrapyd_api = ScrapydAPI(settings.PARSER_URL)

        for category in categories:
            job_id = scrapyd_api.schedule(
                spider='twenty_first_century',
                project='shops',
                category=category.link,
            )
            ScrapyModel.objects.create(category=category, job_id=job_id)
