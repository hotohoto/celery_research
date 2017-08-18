# Celery setup with RabbitMQ and Redis

### RabbitMQ
* https://www.rabbitmq.com/install-standalone-mac.html

```shell
# Install
chown -R $USER /usr/local
brew install rabbitmq
```

```shell
# Start RabbitMQ
sudo rabbitmq-server
```


```shell
# Run RabbitMQ in the background
sudo rabbitmq-server -detached
```

```shell
# Stop
sudo rabbitmqctl stop
```

### Redis (Backend for celery)

```shell
# Install
brew install redis
```

```shell
# Start
redis-server
```

### Celery

```shell
# Install
pip install celery
pip install -U "celery[redis]"
celery -A tasks worker --loglevel=info
```
Requires `tasks.py` to start Celery with.

```shell
# Call the task
python caller.py
```


### References
* http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#choosing-a-broker
* https://www.rabbitmq.com/install-standalone-mac.html
* https://medium.com/@petehouston/install-and-config-redis-on-mac-os-x-via-homebrew-eb8df9a4f298
