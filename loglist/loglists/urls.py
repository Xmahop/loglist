"""Defines url patterns for learning_logs."""

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'logslists'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    path(r'topics/', views.posts, name='posts')
]
