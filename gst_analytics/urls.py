from django.urls import path
from .views import multiply_numbers_async, multiply_numbers_sync

urlpatterns = [
    path('multiply_async/', multiply_numbers_async, name='multiply_numbers_async'),
    path('multiply_sync/', multiply_numbers_sync, name='multiply_numbers_sync'),
]
