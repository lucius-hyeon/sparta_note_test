from wsgiref.util import request_uri
from django.shortcuts import render
# from .models import LogModel
# from django.contrib.auth.decorators import login_required
from .models import AccessLog

# Create your views here.


def introduce(request):
    # case 1
    access_log = AccessLog()
    access_log.location = 'introduce'
    access_log.save()

    # # case 2
    # AccessLog.objects.create(
    #     location='introduce'
    # )

    # 데이터베이스에서 이쁘게 출력하는 방법
    def __str__(self):
        return f'{self.create_at} / {self.location}'


# def myintroduce(request):
#     if request.method == 'GET':
#         log = LogModel()
#         log.location = 'introduce'
#         log.save()

#         location = log.location
#         time = log.created_at

#         content = {
#             "location": location,
#             "create_at": time,
#         }

#         return render(request, 'template2.html', content)
