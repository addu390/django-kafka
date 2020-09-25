from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.serialization import StringDeserializer
from .constants import USER_SCHEMA


class User(object):
    """
    User record
    Args:
        name (str): User's name
        favorite_number (int): User's favorite number
        favorite_color (str): User's favorite color
    """

    def __init__(self, username=None, data=None):
        self.username = username
        self.data = data


def dict_to_user(obj, ctx):
    """
    Converts object literal(dict) to a User instance.
    Args:
        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.
        obj (dict): Object literal(dict)
    """
    if obj is None:
        return None

    return User(username=obj['username'], data=obj['data'])


json_deserializer = JSONDeserializer(USER_SCHEMA, from_dict=dict_to_user)
string_deserializer = StringDeserializer('utf_8')
consumer_conf = {'bootstrap.servers': 'localhost:9092',
                 'key.deserializer': string_deserializer,
                 'value.deserializer': json_deserializer,
                 'group.id': 'django-kafka',
                 'auto.offset.reset': "earliest"}

consumer = DeserializingConsumer(consumer_conf)
consumer.subscribe(['leon'])


# Temporary log-polling
def receive():
    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            user = msg.value()
            if user is not None:
                print("User record {}: username: {}\n"
                      "\tdata: {}\n"
                      .format(msg.key(), user.username,
                              user.data))
        except:
            break

    # consumer.close()
