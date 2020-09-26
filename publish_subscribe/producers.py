from uuid import uuid4
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer

from django_kafka.settings import SCHEMA_REGISTRY_URL
from .constants import USER_SCHEMA, USER_TOPIC
from .transformers import user_to_dict
from .models import UserProducer

schema_registry_conf = {'url': SCHEMA_REGISTRY_URL}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)


def delivery_report(err, msg):
    if err is not None:
        print("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))


json_serializer = JSONSerializer(USER_SCHEMA, schema_registry_client, user_to_dict)
producer_conf = {'bootstrap.servers': 'localhost:9092',
                 'key.serializer': StringSerializer('utf_8'),
                 'value.serializer': json_serializer}
producer = SerializingProducer(producer_conf)


def send(username, data, token):
    user = UserProducer(username=username,
                        data=data,
                        token=token)

    producer.produce(topic=USER_TOPIC, key=str(uuid4()), value=user,
                     on_delivery=delivery_report)
