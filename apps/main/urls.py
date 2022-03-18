# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.main import views

urlpatterns = [
    path('', views.tesst, name='index'),
    path('covid', views.covid, name='covid'),
    path('test', views.tesst, name='tesst'),
    path('video', views.video, name='video'),
    path('world-news', views.worldNews, name='world'),
    path('news', views.News, name='kazakh'),
    path('questions', views.QuestionsList, name='questions'),
    path('note', views.Note, name='note'),
    path('news/<int:pk>/', views.NewsDetail, name='detail'),
]
