from django.shortcuts import render
from .models import Post


def blogpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def blogshow(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'blog/show.html', {'post': post})