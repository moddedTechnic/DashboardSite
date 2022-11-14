"""expenses URL Configuration
"""
from django.urls import path

from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.index, name='index'),
    path('data/income', views.data_income, name='data-income'),
    path('data/expenditure', views.data_expenditure, name='data-expenditure'),
]
