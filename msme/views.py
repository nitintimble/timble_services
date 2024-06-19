# msme/views.py

from django.http import JsonResponse
from .tasks import add
import logging

logger = logging.getLogger(__name__)

def add_numbers(request):
    try:
        x = int(request.GET.get('x', 0))
        y = int(request.GET.get('y', 0))
        result = add.delay(x, y)
        return JsonResponse({'task_id': result.id})
    except Exception as e:
        logger.error(f"Error in add_numbers: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)
