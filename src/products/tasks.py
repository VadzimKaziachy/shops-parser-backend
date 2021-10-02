from core.celery import app


@app.task
def start_handler_product(*args, **kwargs):
    pass
