"""Defines url patterns for learning_logs."""

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'logslists'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    path(r'posts/', views.posts, name='posts'),
    path('new_post/', views.new_post, name='new_post'),
]
