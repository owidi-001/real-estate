from django.urls import path

from .views import agent_dashboard

urlpatterns = [
    path('', agent_dashboard, name="agent_dashboard")
]
