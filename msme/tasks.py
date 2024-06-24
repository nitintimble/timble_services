from celery import shared_task
from .scorecard import calculate_company_score

@shared_task
def async_calculate_company_score(json_file_path):
    return calculate_company_score(json_file_path)

def sync_calculate_company_score(json_file_path):
    return calculate_company_score(json_file_path)

@shared_task
def async_add(x, y):
    return x + y

def sync_add(x, y):
    return x + y
