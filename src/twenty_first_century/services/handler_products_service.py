from typing import NoReturn

from .base_service import BaseService
from ..models import (
    ScrapyModel,
    ProductModel,
    ParserProductModel
)


class HandlerProductsService(BaseService):

    def __init__(self, pk: int) -> NoReturn:
        self.parser_products = list()
        self.scrapy_objects = ScrapyModel.objects.filter(pk=pk)

    def start(self) -> NoReturn:
        if self.scrapy_objects.exists():
            scrapy_object = self.scrapy_objects.first()
            print(scrapy_object.data)
            for new_product in scrapy_object.data:
                product, is_created = ProductModel.objects.get_or_create(
                    name=new_product.get('name'),
                    code=new_product.get('code'),
                    category=scrapy_object.category,
                    defaults={'code': new_product.get('code')}
                )

                self.parser_products.append(ParserProductModel(product=product, price=float(new_product.get('price'))))

            ParserProductModel.objects.bulk_create(self.parser_products)
