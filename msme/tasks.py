from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def add(x, y):
    logger.debug(f"Adding {x} + {y}")
    return x + y
