# task_runner configuration
from task_runner import Celery

class CeleryWorker():
    def make_celery(app):
        celery = Celery(app.import_name,
                        backend = app.config['CELERY_BACKEND'],
                        broker  = app.config['CELERY_BROKER_URL'])
        celery.conf.update(app.config)
        TaskBase = celery.Task
        class ContextTask(TaskBase):
            abstract = True
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)
        celery.Task = ContextTask
        return celery
    
    def __init__(self):
        self.config = {}
        self.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
        self.config['CELERY_BACKEND'] = 'db+postgresql://postgres:kipnit24@localhost/tasks'
        self.config['BROKER_TRANSPORT_OPTIONS'] = {'confirm_publish': True}
        celery = self.make_celery()
        return celery
    
    # def make_celery(app):
    #     task_runner = Celery(app.import_name,
    #                     backend = app.config['CELERY_BACKEND'],
    #                     broker  = app.config['CELERY_BROKER_URL'])
    #     task_runner.conf.update(app.config)
    #     TaskBase = task_runner.Task
    #     class ContextTask(TaskBase):
    #         abstract = True
    #         def __call__(self, *args, **kwargs):
    #             with app.app_context():
    #                 return TaskBase.__call__(self, *args, **kwargs)
    #     task_runner.Task = ContextTask
    #     return task_runner