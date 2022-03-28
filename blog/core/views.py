from django.http import HttpResponse
from django.shortcuts import render
from blog_post.models import Post
from blog_post.models import Category


def front_page(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    if request.method == "GET" and 'category' in request.GET:
        value_category = Category.objects.get(title=request.GET['category'])
        posts = Post.objects.filter(category=value_category)
        return render(request, 'core/frontpage.html', {'posts': posts, 'categories': categories})
    return render(request, 'core/frontpage.html', {'posts': posts, 'categories': categories})


def about_page(request):
    return render(request, 'core/aboutpage.html')


def robots_txt(request):
    text = [
        "User-agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
