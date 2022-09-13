from django.urls import path

from .views import tenant_dashboard

urlpatterns = [
    path('', tenant_dashboard, name="tenant_dashboard")
]
