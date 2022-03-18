from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader

from apps.main.models import Video, Blog, Questions, Covid


def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('site/main.html')
    return HttpResponse(html_template.render(context, request))


def video(request):
    context = {'segment': 'video'}

    video_list = Video.objects.all()
    context['list'] = video_list
    html_template = loader.get_template('site/video.html')
    return HttpResponse(html_template.render(context, request))


def tesst(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('site/geography.html')
    return HttpResponse(html_template.render(context, request))

def covid(request):
    context = {'segment': 'covid'}

    html_template = loader.get_template('site/includes/covid-19.html')
    return HttpResponse(html_template.render(context, request))


def worldNews(request):
    context = {'segment': 'world'}

    blog_list = Blog.objects.filter(category_id=1)
    main_list = blog_list[0:9]
    other_list = blog_list[9:len(blog_list)]
    context['main_list'] = main_list
    context['other_list'] = other_list
    html_template = loader.get_template('site/world-news.html')
    return HttpResponse(html_template.render(context, request))


def News(request):
    context = {'segment': 'kazakh'}

    blog_list = Blog.objects.filter(category_id=1)
    main_list = blog_list[0:9]
    other_list = blog_list[9:len(blog_list)]
    context['main_list'] = main_list
    context['other_list'] = other_list
    html_template = loader.get_template('site/kazakhstan-news.html')
    return HttpResponse(html_template.render(context, request))


def NewsDetail(request, pk):
    context = {'segment': 'kazakh'}

    blog = Blog.objects.get(pk=pk)
    if blog:
        context['blog'] = blog
        category_list = Blog.objects.filter(category=blog.category).exclude(pk=blog.pk)
        popular_list = Blog.objects.filter(status_id=2, category=blog.category).exclude(pk=blog.pk)
        context['category_list'] = category_list
        context['popular_list'] = popular_list[0:9]
        html_template = loader.get_template('site/news-detail.html')
        return HttpResponse(html_template.render(context, request))
    else:
        return redirect('index')


def QuestionsList(request):
    context = {'segment': 'question'}

    questions = Questions.objects.all()
    questions_list = questions
    context['list'] = questions_list
    html_template = loader.get_template('site/questions.html')
    return HttpResponse(html_template.render(context, request))


def Note(request):
    context = {'segment': 'note'}

    html_template = loader.get_template('site/note.html')
    return HttpResponse(html_template.render(context, request))
