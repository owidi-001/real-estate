from django.db import models

# Create your models here.
from user.models import User


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
