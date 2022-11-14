"""main URL Configuration
"""
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('favicon.ico', views.favicon, name='favicon'),
]
