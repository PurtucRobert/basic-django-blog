from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .models import Post
from .models import Category
from .forms import CommentForm
# Create your views here.


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail", slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog_post/detail.html', {'post': post, 'form': form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    return render(request, 'blog_post/category.html', {'category': category})
