# Django Kafka `Work In Progress 🚁`
Django + Kafka 🚀

#### Kafka
- Simply put, Kafka is a distributed publish-subscribe messaging system that maintains feeds of messages in partitioned and replicated topics. 
- In the simplest way there are three players in the Kafka ecosystem: producers, topics (run by brokers) and consumers.

#### Installation Zookeeper (MacOS)
- `brew install zookeeper`
- Where is installation directory of zookeeper : `/usr/local/Cellar/zookeeper`

#### Start Zookeeper
- In foreground `zkServer start`
- In background `brew services start zookeeper`

#### Installation Kafka (MacOS)
- `brew install kafka`
- Where is installation directory of Kafka : `/usr/local/Cellar/kafka`

#### Start Kafka
- In foreground `brew services start kafka`
- In background `zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties & kafka-server-start /usr/local/etc/kafka/server.properties`

#### Tip
- Run ZK and Kafka `zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties & kafka-server-start /usr/local/etc/kafka/server.properties`

For details on how to set-up a django project with best practices: https://pyblog.xyz/django-initial-setup/

#### Settings
- Update Kafka - host and port in `settings.py` 
```
LOGPIPE = {
    'OFFSET_BACKEND': 'logpipe.backend.kafka.ModelOffsetStore',
    'CONSUMER_BACKEND': 'logpipe.backend.kafka.Consumer',
    'PRODUCER_BACKEND': 'logpipe.backend.kafka.Producer',
    'KAFKA_BOOTSTRAP_SERVERS': [
        'kafka:9092'
    ],
    'KAFKA_CONSUMER_KWARGS': {
        'group_id': 'django-logpipe',
    },

    # Optional Settings
    # 'KAFKA_SEND_TIMEOUT': 10,
    # 'KAFKA_MAX_SEND_RETRIES': 0,
    # 'MIN_MESSAGE_LAG_MS': 0,
    # 'DEFAULT_FORMAT': 'json',
}
```

#### Installation
- `pip install django-logpipe`
- Documentation: https://pypi.org/project/django-logpipe/

- Add `logpipe` to your installed apps.
```
INSTALLED_APPS = [
    ...
    'logpipe',
    ...
]
```
- Run migrations to store Kafka log position offsets: `python manage.py migrate logpipe`
- To process messages for all consumers automatically in a round-robin fashion: `python manage.py run_kafka_consumer` 

###### Note: The project is an example for  Django application as a producer/consumer 😋 
