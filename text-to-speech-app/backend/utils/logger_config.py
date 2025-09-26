import logging
import logging.config
import os
import re
from pathlib import Path

# Setup basic configuration
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
LOG_RETENTION_DAYS = int(os.environ.get("LOG_RETENTION_DAYS", 10))
LOG_DIR = os.environ.get("LOG_DIR", "logs")

Path(LOG_DIR).mkdir(exist_ok=True, parents=True)

class SensitiveDataFilter(logging.Filter):
    def filter(self, record):
        if hasattr(record, 'msg') and isinstance(record.msg, str):
            record.msg = re.sub(r'(api_key|token)=[\w-]+', r'\1=[REDACTED]', record.msg, flags=re.IGNORECASE)
            # record.msg = re.sub(r'[\w.+-]+@[\w-]+\.[\w.-]+', '[EMAIL_REDACTED]', record.msg)
        return True

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "filters": {
        "sensitive_data_filter": {
            "()": SensitiveDataFilter,
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": LOG_LEVEL,
            "stream": "ext://sys.stdout",
            "filters": ["sensitive_data_filter"],
        },
        "file": {
            "formatter": "default",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": LOG_LEVEL,
            "filename": os.path.join(LOG_DIR, "app.log"),
            "when": "midnight",
            "backupCount": LOG_RETENTION_DAYS,
            "encoding": "utf-8",
            "filters": ["sensitive_data_filter"],
        },
    },
    "loggers": {
        "app": {
            "handlers": ["file", "console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "uvicorn": {
            "handlers": ["file", "console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "fastapi": {
            "handlers": ["file", "console"],
            "level": LOG_LEVEL,
            "propagate": False,
        }
    },
    "root": {
        "handlers": ["console", "file"],
        "level": LOG_LEVEL,
    }
}

logging.config.dictConfig(LOGGING_CONFIG)

def get_app_logger(name):
    """
    Get a logger with the standard configuration
    
    Args:
        name: The name for the logger, typically __name__
    
    Returns:
        A configured logger instance
    """
    return logging.getLogger(name)

app_logger = get_app_logger("backend-app")
