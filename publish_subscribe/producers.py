from logpipe import Producer
from .models import MessageSerializer


def send(message):
    producer = Producer('message', MessageSerializer)
    producer.send(message)
