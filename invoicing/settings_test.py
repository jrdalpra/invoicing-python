from .settings import *

import logging


logging.basicConfig()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {
        "": {"handlers": ["console"], "level": "INFO"},
        "invoicing": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
    },
}
