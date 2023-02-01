import logging.config


log_config = {
    "version": 1,
    "formatters": {
        "formatter": {
            "format": '%(asctime)s - %(levelname)s - %(message)s',
            "datefmt": '%d-%b-%y %H:%M:%S',
        },
        "trace_formatter": {
            "format": '%(asctime)s - %(message)s',
            "datefmt": '%d-%b-%y %H:%M:%S',
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "formatter": "formatter",
            "filename": "app.log"
        },
        "trace_handler": {
            "class": "logging.StreamHandler",
            "formatter": "trace_formatter",
        },
    },
    "loggers": {
        "log": {
            "handlers": ["file_handler", "trace_handler"],
            "level": "DEBUG",
        },
    },
}


logging.config.dictConfig(log_config)
logger = logging.getLogger("log")
