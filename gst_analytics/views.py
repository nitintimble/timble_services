from django.http import JsonResponse
from .tasks import multiply
import logging

logger = logging.getLogger(__name__)

# Asynchronous view using Celery
def multiply_numbers_async(request):
    try:
        x = int(request.GET.get('x', 0))
        y = int(request.GET.get('y', 0))
        result = multiply.delay(x, y)  # Asynchronous task
        return JsonResponse({'task_id': result.id})
    except Exception as e:
        logger.error(f"Error in multiply_numbers_async: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

# Function to get the result of an async task
def get_task_result(request, task_id):
    try:
        result = AsyncResult(task_id)
        response = {
            'task_id': task_id,
            'status': result.status,
            'result': result.result if result.status == 'SUCCESS' else None
        }
        return JsonResponse(response)
    except Exception as e:
        logger.error(f"Error in get_task_result: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

# Synchronous view
def multiply_numbers_sync(request):
    try:
        x = int(request.GET.get('x', 0))
        y = int(request.GET.get('y', 0))
        result = multiply(x, y)  # Synchronous task
        return JsonResponse({'result': result})
    except Exception as e:
        logger.error(f"Error in multiply_numbers_sync: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)
