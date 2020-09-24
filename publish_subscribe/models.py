from django.db import models
from rest_framework import serializers
import uuid


class Message(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    username = models.CharField(max_length=200)
    data = models.TextField()


class MessageSerializer(serializers.ModelSerializer):
    MESSAGE_TYPE = 'message'
    VERSION = 1
    KEY_FIELD = 'uuid'

    class Meta:
        model = Message
        fields = ['uuid', 'username', 'data']

    @classmethod
    def lookup_instance(cls, uid, **kwargs):
        try:
            return Message.objects.get(uuid=uid)
        except models.Message.DoesNotExist:
            pass
