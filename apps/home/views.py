# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import random
import string

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse

from apps.home.models import *
from apps.main.models import *


def index(request):
    context = {'segment': 'admin-index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


def news(request):
    context = {'segment': 'admin-news'}

    news_list = Blog.objects.all()

    context['list'] = news_list

    html_template = loader.get_template('home/news/news-list.html')
    return HttpResponse(html_template.render(context, request))


def newsAdd(request):
    context = {'segment': 'admin-news'}

    status_list = Status.objects.all()
    type_list = Type.objects.all()
    category_list = Category.objects.all()

    context['status_list'] = status_list
    context['type_list'] = type_list
    context['category_list'] = category_list

    if request.method == "POST":
        print(request.POST)
        title = request.POST['title']
        description = request.POST['description']
        sub_title = request.POST['sub_title']
        sub_description = request.POST['sub_description']
        p_image = None
        if request.FILES:
            p_image = request.FILES['p_image']
        status = request.POST['status']
        category = request.POST['category']
        type = request.POST['type']

        blog = Blog.objects.create(title=title, description=description, subtitle=sub_title,
                                   sub_description=sub_description, image=p_image,
                                   status_id=status, category_id=category, type_id=type)
        blog.save()

    html_template = loader.get_template('home/news/add.html')
    return HttpResponse(html_template.render(context, request))


def newsEdit(request, pk):
    context = {'segment': 'admin-news'}

    status_list = Status.objects.all()
    type_list = Type.objects.all()
    category_list = Category.objects.all()

    context['status_list'] = status_list
    context['type_list'] = type_list
    context['category_list'] = category_list

    blog = Blog.objects.get(pk=pk)
    context['blog'] = blog

    if blog is None:
        return redirect('index')

    if request.method == "POST":
        print(request.POST)
        title = request.POST['title']
        description = request.POST['description']
        sub_title = request.POST['sub_title']
        sub_description = request.POST['sub_description']
        if request.FILES:
            p_image = request.FILES['p_image']
            blog.image = p_image
        status = request.POST['status']
        category = request.POST['category']
        type = request.POST['type']

        blog.title = title
        blog.description = description
        blog.subtitle = sub_title
        blog.sub_description = sub_description

        blog.status_id = status
        blog.category_id = category
        blog.type_id = type
        blog.save()
        return redirect('news')

    html_template = loader.get_template('home/news/edit.html')
    return HttpResponse(html_template.render(context, request))


def newsDelete(request, pk):
    blog = Blog.objects.get(pk=pk)

    if blog is None:
        return redirect('news')
    blog.delete()

    return redirect('news')


def video(request):
    context = {'segment': 'admin-video'}

    video_list = Video.objects.all()

    context['list'] = video_list

    html_template = loader.get_template('home/video/video-list.html')
    return HttpResponse(html_template.render(context, request))


def videoAdd(request):
    context = {'segment': 'admin-video'}

    if request.method == "POST":
        name = request.POST['name']
        link = request.POST['link']
        video = Video.objects.create(name=name, link=link)
        video.save()
        return redirect('video')

    html_template = loader.get_template('home/video/add.html')
    return HttpResponse(html_template.render(context, request))


def videoEdit(request, pk):
    context = {'segment': 'admin-video'}

    video = Video.objects.get(pk=pk)

    if video is None:
        return redirect('video')

    context['video'] = video

    if request.method == "POST":
        name = request.POST['name']
        link = request.POST['link']
        video.name = name
        video.link = link
        video.save()
        return redirect('video')

    html_template = loader.get_template('home/video/edit.html')
    return HttpResponse(html_template.render(context, request))


def videoDelete(request, pk):
    video = Video.objects.get(pk=pk)

    if video is None:
        return redirect('video')
    video.delete()

    return redirect('video')


def qaList(request):
    context = {'segment': 'admin-qa'}

    qa_list = Questions.objects.all()

    context['list'] = qa_list

    html_template = loader.get_template('home/question/list.html')
    return HttpResponse(html_template.render(context, request))


def qaAdd(request):
    context = {'segment': 'admin-qa'}

    if request.method == "POST":
        question = request.POST['question']
        answer = request.POST['answer']
        qa = Questions.objects.create(question=question, answer=answer)
        qa.save()
        return redirect('qa')

    html_template = loader.get_template('home/question/add.html')
    return HttpResponse(html_template.render(context, request))


def qaEdit(request, pk):
    context = {'segment': 'admin-qa'}

    qa = Questions.objects.get(pk=pk)

    if qa is None:
        return redirect('qa')

    context['qa'] = qa

    if request.method == "POST":
        question = request.POST['question']
        answer = request.POST['answer']
        qa.question = question
        qa.answer = answer
        qa.save()
        return redirect('qa')

    html_template = loader.get_template('home/question/edit.html')
    return HttpResponse(html_template.render(context, request))


def qaDelete(request, pk):
    qa = Questions.objects.get(pk=pk)

    if qa is None:
        return redirect('qa')
    qa.delete()

    return redirect('qa')
