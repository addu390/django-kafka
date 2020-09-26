from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.serialization import StringDeserializer
from .constants import USER_SCHEMA
from .transformers import dict_to_user
import logging
import traceback


def receive():
    json_deserializer = JSONDeserializer(USER_SCHEMA, from_dict=dict_to_user)
    string_deserializer = StringDeserializer('utf_8')
    consumer_conf = {'bootstrap.servers': 'localhost:9092',
                     'key.deserializer': string_deserializer,
                     'value.deserializer': json_deserializer,
                     'group.id': 'django-kafka',
                     'auto.offset.reset': "earliest"}

    consumer = DeserializingConsumer(consumer_conf)
    consumer.subscribe(['leon'])
    try:
        msg = consumer.poll(timeout=5.0)
        if msg is not None:
            user = msg.value()
            if user is not None:
                print("User record {}: username: {}\n"
                      "\tdata: {}\n"
                      .format(msg.key(), user.username,
                              user.data))

    except Exception as e:
        print('An exception occurred: {}'.format(e))
        logging.error(traceback.format_exc())

