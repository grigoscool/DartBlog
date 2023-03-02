from django.shortcuts import render

from .models import Post


def index(request):
    return render(request, 'blog/index.html')


def show_cat(request, slug):
    return render(request, 'blog/cat.html')
