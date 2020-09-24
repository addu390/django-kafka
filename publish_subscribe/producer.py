from logpipe import Producer
from .models import Person, PersonSerializer


def send(first_name, last_name):
    person = Person.objects.create(first_name=first_name, last_name=last_name)
    producer = Producer('people', PersonSerializer)
    producer.send(person)
