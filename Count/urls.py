from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from Count import urls

from . import views

urlpatterns = [
    path('home/', views.index),
    path('home/result', views.show_result)
]
