from celery import shared_task

from core.celery import app

from .services import (
    ParsingService,
    HandlerProductsService,
)


@shared_task
def start_parsing_shop():
    """
    Task for start parser shop.
    :return: not return
    """
    ParsingService.execute({})


@app.task
def start_handler_product(id: int):
    """
    Task for handler products.
    :param id: int
    :return: not return
    """
    HandlerProductsService.execute({'id': id})
