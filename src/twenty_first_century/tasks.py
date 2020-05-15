from celery import shared_task

from core.celery import app

from .services.parsing_service import ParsingService
from .services.handler_products_service import HandlerProductsService


@shared_task
def start_parsing_shop():
    parsing_service = ParsingService()
    parsing_service.start()


@app.task
def start_handler_product(pk: int):
    handler_products_service = HandlerProductsService(pk=pk)
    handler_products_service.start()