from django.apps import AppConfig
from logpipe import Consumer, register_consumer
from .models import PersonSerializer


class PublishSubscribeConfig(AppConfig):
    name = 'publish_subscribe'


@register_consumer
def build_person_consumer():
    consumer = Consumer('people')
    consumer.register(PersonSerializer)
    return consumer
