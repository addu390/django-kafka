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

For details on how to set-up a django project with best practices: https://pyblog.xyz/django-initial-setup/

#### Settings
- Update Kafka - host and port in `settings.py` 
```
KAFKA_BOOTSTRAP_SERVER = 'http://localhost:9092'
```

###### Note: The project is an example for  Django application as a producer/consumer 😋 
