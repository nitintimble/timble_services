from django.http import JsonResponse
from .tasks import multiply

def multiply_numbers(request):
    try:
        x = int(request.GET.get('x', 0))
        y = int(request.GET.get('y', 0))
        result = multiply.delay(x, y)
        return JsonResponse({'task_id': result.id})
    except Exception as e:
        logger.error(f"Error in multiply_numbers: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)
