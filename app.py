from flask import Flask
from routes.mongo_router import mongo
from routes.puppet_router import puppet
from celery_tasks.make import make_celery
#from celery_tasks.tasks import reverse

app = Flask(__name__)

# celery configuration
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_BACKEND'] = 'redis://localhost:6379/0'
# blueprint configuration
app.register_blueprint(mongo)
app.register_blueprint(puppet)

celery = make_celery(app)

@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'I sent an async reqeust!'
    
@celery.task(name='app.reverse')
def reverse(string):
    return string[::-1]

if __name__ == '__main__':
    app.run(debug=True)