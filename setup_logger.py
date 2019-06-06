import logging
import logging.config
import logging.handlers
# logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
# logger = logging.getLogger('spam')
#
# mlogger =


CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'debug_file': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'debug': {
            'handlers':['debug_file', 'console'],
            'propagate': True,
            'level': 'DEBUG'
        },
        # 'django.request': {
        #     'handlers': ['mail_admins'],
        #     'level': 'ERROR',
        #     'propagate': False,
        # },
        # 'myproject.custom': {
        #     'handlers': ['console', 'mail_admins'],
        #     'level': 'INFO',
        #     'filters': ['special']
        # }
    }
}

logging.config.dictConfig(CONFIG)
logger = logging.getLogger('debug')