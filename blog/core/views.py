from django.shortcuts import render

# Create your views here.

from blog_post.models import Post


def front_page(request):
    posts = Post.objects.all()
    return render(request, 'core/frontpage.html', {'posts': posts})


def about_page(request):
    return render(request, 'core/aboutpage.html')
