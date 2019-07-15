from __future__ import absolute_import, unicode_literals
from task_runner.celery import worker

@worker.task
def reverse(string):
    return string[::-1]