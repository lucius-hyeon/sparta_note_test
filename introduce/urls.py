from django.urls import path
from introduce import views

# urlpatterns = [
#     path('introduce/', views.myintroduce, name='myintroduce'),
# ]
urlpatterns = [
    path('introduce/', views.introduce, name='introduce'),
]
