from django.http import JsonResponse
from .tasks import async_calculate_company_score, sync_calculate_company_score, async_add, sync_add
from .scorecard import calculate_company_score
import json

# Synchronous views
def calculate_company_score_sync(request):
    json_file_path = request.GET.get('json_file_path')
    result = sync_calculate_company_score(json_file_path)
    return JsonResponse(result)

def add_numbers_sync(request):
    x = int(request.GET.get('x', 0))
    y = int(request.GET.get('y', 0))
    result = sync_add(x, y)
    return JsonResponse({'result': result})

# Asynchronous views
def calculate_company_score_async(request):
    json_file_path = request.GET.get('json_file_path')
    task = async_calculate_company_score.delay(json_file_path)
    return JsonResponse({'task_id': task.id})

def add_numbers_async(request):
    x = int(request.GET.get('x', 0))
    y = int(request.GET.get('y', 0))
    task = async_add.delay(x, y)
    return JsonResponse({'task_id': task.id})

# View to get task result
from celery.result import AsyncResult

def get_task_result(request, task_id):
    result = AsyncResult(task_id)
    if result.state == 'SUCCESS':
        response = result.result
    else:
        response = {'state': result.state}
    return JsonResponse(response)
