from django.db import models

# Create your models here.


class LogModel(models.Model):
    class Meta:
        db_table = "tweet"

    location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
