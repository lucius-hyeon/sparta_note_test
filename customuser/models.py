from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomModel(AbstractUser):
    class Meta:
        db_table = 'customuser'

    address = models.TextField(
        max_length=500, blank=True, null=None)
    bio = models.TextField(max_length=500, blank=True, null=None)
