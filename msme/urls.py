from django.urls import path
from .views import add_numbers_async, add_numbers_sync

urlpatterns = [
    path('add_async/', add_numbers_async, name='add_numbers_async'),
    path('add_sync/', add_numbers_sync, name='add_numbers_sync'),
]
