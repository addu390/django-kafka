# Django Kafka `Work In Progress 🚁`
Django + Kafka 🚀

#### Confluent Installation (Local set-up)
- `pip install confluent-kafka`
- Download confluent platform from: https://www.confluent.io/download/ and unzip the file.
- `export CONFLUENT_HOME=<path-to-confluent>`
- `export PATH=$PATH:$CONFLUENT_HOME/bin`
- `$CONFLUENT_HOME/bin/confluent-hub install \ --no-prompt confluentinc/kafka-connect-datagen:latest`

The output would be:
```
Running in a "--no-prompt" mode
...
Completed
```

- Start the service: `confluent local start`
The output should resemble:
```
Starting Zookeeper
Zookeeper is [UP]
Starting Kafka
Kafka is [UP]
Starting Schema Registry
Schema Registry is [UP]
Starting Kafka REST
Kafka REST is [UP]
Starting Connect
Connect is [UP]
Starting KSQL Server
KSQL Server is [UP]
Starting Control Center
Control Center is [UP]
```
- Stop services: `confluent local stop`

Or set-up Kafka and Zookeeper Separately
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

For details on how to set-up a django project with best practices: https://pyblog.xyz/django-initial-setup/

#### Celery Installation - For polling
- `pip install amqp`
- `pip install celery==4.4.0` (Note: Celery 5.0 is not compatible with django-celery-beat)
- `pip install django-celery-beat`

- Start worker and beat `celery -A django_kafka beat -l INFO -S django`
- Start RabbitMQ `brew services start rabbitmq`

#### Update settings.py
```
INSTALLED_APPS = [
    ...,
    'django_celery_beat',
]
```
- Run migrations: `python manage.py migrate django_celery_beat` 

Note: In this project, the same Django project is the Producer and Consumer, but you can choose you have a standalone consumer.

#### Have a look at:
- https://docs.confluent.io/current/getting-started.html 
- https://www.instaclustr.com/apache-kafka-architecture/
- https://github.com/confluentinc/confluent-kafka-python
- https://docs.confluent.io/current/schema-registry/index.html
- https://docs.confluent.io/current/quickstart/ce-quickstart.html

###### Note: The project is an example for  Django application as a producer/consumer 😋 
