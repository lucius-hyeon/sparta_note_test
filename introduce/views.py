from django.shortcuts import render


def myintroduce(request):
    if request.method == 'GET':
        # return render(request, 'introduce/template.html')
        return render(request, 'templates/template2.html')


# Create your views here.
