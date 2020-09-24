from django.db import models
from rest_framework import serializers
import uuid


class Person(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class PersonSerializer(serializers.ModelSerializer):
    MESSAGE_TYPE = 'person'
    VERSION = 1
    KEY_FIELD = 'uuid'

    class Meta:
        model = Person
        fields = ['uuid', 'first_name', 'last_name']

    @classmethod
    def lookup_instance(cls, uuid, **kwargs):
        try:
            return Person.objects.get(uuid=uuid)
        except models.Person.DoesNotExist:
            pass
