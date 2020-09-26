from django.apps import AppConfig


class PublishSubscribeConfig(AppConfig):
    name = 'publish_subscribe'

    def ready(self):
        from .consumer import receive
        # receive()

