This app also requires rabbitmq-server as a message broker for celery
This app also requires redis to be running as a database for celery taks persistence.
when installing redis make sure to read https://redis.io/topics/admin and make the appropriate configuration changes.

asynchronous tasks are handled by celery.  celery will provide a unique ID, which the front-end can poll for asynchronous-task status.