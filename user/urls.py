from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import signup, signin, home

urlpatterns = [
    path('', home, name='home'),
    path('register/', signup, name='register'),
    path('login/', signin, name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
    path('profile/', signup, name='profile'),
]
