from __future__ import absolute_import, unicode_literals
from celery import Celery

# the message queue is hosted by rabbitmq-server
worker = Celery('proj',
              broker='amqp://localhost//',
              backend= 'db+postgresql://postgres:kipnit24@localhost/tasks',
              include=['proj.tasks'])
worker.conf.update(
    result_expires=3600,
)

if __name__=='__main__':
    worker.start()