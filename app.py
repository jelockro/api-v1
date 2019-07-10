#!/usr/bin/env python3

from flask import Flask
from routes.mongo_router import mongo
from routes.puppet_router import puppet
from proj import tasks
try:
    from hiera_evolv_routes import hiera_evolv
except ImportError:
    print("hiera_evolv routes don't exist yet")
try:
    from hiera_vision_routes import hiera_vision
except ImportError:
    print("hiera_vision routes don't exist yet")
from upgrade import upgrade
from setup_logger import logger
from hiera_avatar_routes import hiera_avatar
from helpers.checks import checks
app = Flask(__name__)


# blueprint configuration
app.register_blueprint(mongo)
app.register_blueprint(puppet)
app.register_blueprint(hiera_avatar)
app.register_blueprint(checks)
app.register_blueprint(upgrade)
try:
    app.register_blueprint(hiera_evolv)
except NameError:
    print('hiera_evolv blueprint not implemented.')
try:
    app.register_blueprint(hiera_vision)
except NameError:
    print('hiera_vision blueprint not implemented.')
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