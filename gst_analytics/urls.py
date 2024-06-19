from django.urls import path
from .views import multiply_numbers_async, multiply_numbers_sync, get_task_result

urlpatterns = [
    path('multiply_async/', multiply_numbers_async, name='multiply_numbers_async'),
    path('multiply_sync/', multiply_numbers_sync, name='multiply_numbers_sync'),
    path('task_result/<str:task_id>/', get_task_result, name='get_task_result'),  # Add this line
]
