from .views import index,person
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('person/',person),
    path('person/<int:pid>',person)
]
