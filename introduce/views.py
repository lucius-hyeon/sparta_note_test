from wsgiref.util import request_uri
from django.shortcuts import render
from .models import LogModel
from django.contrib.auth.decorators import login_required


def myintroduce(request):
    if request.method == 'GET':
        log = LogModel()
        log.location = 'introduce'
        log.save()

        location = log.location
        time = log.created_at

        content = {
            "location": location,
            "create_at": time,
        }

        return render(request, 'template2.html', content)


# Create your views here.
