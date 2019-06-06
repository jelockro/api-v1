#!/usr/bin/env python

from flask import Flask
from routes.mongo_router import mongo
from routes.puppet_router import puppet
from proj import tasks

from setup_logger import logger

app = Flask(__name__)


# blueprint configuration
app.register_blueprint(mongo)
app.register_blueprint(puppet)
app.debug = True


@app.route('/')
def index():
    return 'Api Gateway'

@app.route('/process/<name>')
def process(name):
    tasks.reverse.delay(name)
    return 'I sent an async reqeust!'


#@app.route('/status/<celery_task_id>')


# @celery.task(name='app.reverse')
# def reverse(string):
#     return string[::-1]

if __name__ == '__main__':
    logger.info('Started')
    app.run(host='0.0.0.0', port=5000)