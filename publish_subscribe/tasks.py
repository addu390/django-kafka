from celery import shared_task
from .consumer import receive


@shared_task
def send_summary():
    receive()
