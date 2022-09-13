from django.urls import path

from .views import landlord_dashboard

urlpatterns = [
    path('', landlord_dashboard, name="landlord_dashboard")
]
