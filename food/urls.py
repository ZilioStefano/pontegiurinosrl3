# from django.conf.urls import url
from django.urls import path
from food import views


urlpatterns = [
    path('', views.index2, name='index'),
]