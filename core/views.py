from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView

def index(request):
    Posts = Post.objects.all()
    context = {
        'posts': Post
    }
    return render(request, 'index.html', context)

