# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path

from apps.authentication.views import login_view
from apps.home import views

urlpatterns = [
    path('', views.index, name='admin-index'),
    path('home', login_view, name='home'),
    path('news', views.news, name='news'),
    path('news-add', views.newsAdd, name='news-add'),
    path('news/<int:pk>', views.newsEdit, name='news-edit'),
    path('news/<int:pk>/delete', views.newsDelete, name='news-delete'),
    path('video', views.video, name='admin-video'),
    path('video-add', views.videoAdd, name='video-add'),
    path('video/<int:pk>', views.videoEdit, name='video-edit'),
    path('video/<int:pk>/delete', views.videoDelete, name='video-delete'),
    path('qa', views.qaList, name='qa'),
    path('qa-add', views.qaAdd, name='qa-add'),
    path('qa/<int:pk>', views.qaEdit, name='qa-edit'),
    path('qa/<int:pk>/delete', views.qaDelete, name='qa-delete'),
]
