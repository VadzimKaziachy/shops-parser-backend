from typing import NoReturn

from django.conf import settings
from scrapyd_api import ScrapydAPI

from .base_service import BaseService

from ..models import CategoryModel, ScrapyModel


class ParsingService(BaseService):

    def __init__(self) -> NoReturn:
        self.spider = 'twenty_first_century',
        self.project = 'shops',
        self.categories = CategoryModel.objects.all()
        self.scrapyd_api = ScrapydAPI(settings.PARSER_URL)

    def start(self) -> NoReturn:
        for category in self.categories:
            job_id = self.scrapyd_api.schedule(
                spider=self.spider,
                project=self.project,
                category=category.link,
            )
            ScrapyModel.objects.create(category=category, job_id=job_id)
