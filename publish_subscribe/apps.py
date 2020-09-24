from django.apps import AppConfig
from logpipe import Consumer, register_consumer
from .models import MessageSerializer


class PublishSubscribeConfig(AppConfig):
    name = 'publish_subscribe'


@register_consumer
def build_message_consumer():
    consumer = Consumer('message')
    consumer.register(MessageSerializer)
    return consumer
