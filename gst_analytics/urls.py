from django.urls import path
from .views import multiply_numbers

urlpatterns = [
    path('multiply/', multiply_numbers, name='multiply_numbers'),
]
