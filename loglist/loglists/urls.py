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
    path('posts/<int:post_id>/', views.post, name='post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('posts/tag_list/', views.tag_list, name='tag_list'),
    path('posts/<str:slug>', views.tag_detail, name='tag_detail')
    ]
