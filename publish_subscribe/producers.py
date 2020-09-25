from uuid import uuid4
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from .constants import USER_SCHEMA

schema_registry_conf = {'url': 'http://localhost:8081'}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)


class User(object):
    """
    User record
    Args:
        username (str): User's name
        data (int): User's data
        token(str): User's address; confidential
    """

    def __init__(self, username, token, data):
        self.username = username
        self.data = data
        # token should not be serialized, see user_to_dict()
        self._token = token


def user_to_dict(user, ctx):
    """
    Returns a dict representation of a User instance for serialization.
    Args:
        user (User): User instance.
        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.
    Returns:
        dict: Dict populated with user attributes to be serialized.
    """
    # User._token must not be serialized; omit from dict
    return dict(username=user.username,
                data=user.data)


def delivery_report(err, msg):
    """
    Reports the failure or success of a message delivery.
    Args:
        err (KafkaError): The error that occurred on None on success.
        msg (Message): The message that was produced or failed.
    Note:
        In the delivery report callback the Message.key() and Message.value()
        will be the binary format as encoded by any configured Serializers and
        not the same object that was passed to produce().
        If you wish to pass the original object(s) for key and value to delivery
        report callback we recommend a bound callback or lambda where you pass
        the objects along.
    """
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
    user = User(username=username,
                data=data,
                token=token)

    producer.produce(topic='leon', key=str(uuid4()), value=user,
                     on_delivery=delivery_report)
