from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def multiply(x, y):
    logger.debug(f"Multiplying {x} * {y}")
    return x * y
