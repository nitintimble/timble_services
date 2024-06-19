from django.http import JsonResponse
from .tasks import add
import logging

logger = logging.getLogger(__name__)

# Asynchronous view using Celery
def add_numbers_async(request):
    try:
        x = int(request.GET.get('x', 0))
        y = int(request.GET.get('y', 0))
        result = add.delay(x, y)  # Asynchronous task
        return JsonResponse({'task_id': result.id})
    except Exception as e:
        logger.error(f"Error in add_numbers_async: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

# Synchronous view
def add_numbers_sync(request):
    try:
        x = int(request.GET.get('x', 0))
        y = int(request.GET.get('y', 0))
        result = add(x, y)  # Synchronous task
        return JsonResponse({'result': result})
    except Exception as e:
        logger.error(f"Error in add_numbers_sync: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)
