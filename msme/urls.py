from django.urls import path
from .views import (
    calculate_company_score_sync, calculate_company_score_async, get_task_result,
    add_numbers_sync, add_numbers_async
)

urlpatterns = [
    path('calculate_company_score_sync/', calculate_company_score_sync, name='calculate_company_score_sync'),
    path('calculate_company_score_async/', calculate_company_score_async, name='calculate_company_score_async'),
    path('task_result/<str:task_id>/', get_task_result, name='get_task_result'),
    path('add_sync/', add_numbers_sync, name='add_numbers_sync'),
    path('add_async/', add_numbers_async, name='add_numbers_async'),
]
