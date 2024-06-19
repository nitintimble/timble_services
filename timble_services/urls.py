# timble_services/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('msme/', include('msme.urls')),
    path('gst_analytics/', include('gst_analytics.urls')),
]
