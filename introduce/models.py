from django.db import models

# Create your models here.


# class LogModel(models.Model):
#     class Meta:
#         db_table = "AccessLog"

#     location = models.CharField(max_length=256)
#     created_at = models.DateTimeField(auto_now_add=True)


class AccessLog(models.Model):
    class Meta:
        db_table = 'AccessLog'

    location = models.CharField('접속 경로', max_length=256)
    created_at = models.DateTimeField('접속 시간', auto_now_add=True)
