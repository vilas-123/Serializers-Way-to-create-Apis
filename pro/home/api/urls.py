
from django.contrib import admin
from django.urls import path

from pro.home.views import index

urlpatterns = [
    path('index/', index),
]
