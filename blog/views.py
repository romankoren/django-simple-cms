from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request,
    'blog/post_list.html',
    context)

def post_list(request):
    return render(request, 'blog/post_list.html', {})


def post_detail(request, pk):
    # post = get_object_or_404(Post, int(pk)
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(
            request,
            'blog/post_detail.html',
            context
            )
