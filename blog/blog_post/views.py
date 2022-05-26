from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .models import Post
from .models import Category
from .forms import CommentForm, PostForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()
    return render(request, "blog_post/detail.html", {"post": post, "form": form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    return render(request, "blog_post/category.html", {"category": category})


@login_required
def add_blog_post(request):
    if request.method == "POST":
        form_data = PostForm(request.POST, request.FILES)
        print(form_data)
        print(request.POST)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect("front_page")
        return render(request, "blog_post/add_blog_post.html")
    else:
        categories = Category.objects.all()
        return render(
            request, "blog_post/add_blog_post.html", {"categories": categories}
        )


@login_required
def edit_blog_post(request, category_slug, slug):
    if request.method == "GET":
        post = Post.objects.get(slug=slug)
        categories = Category.objects.all()
        if post:
            return render(
                request,
                "blog_post/edit_blog_post.html",
                {"post": post, "categories": categories},
            )
    if request.method == "POST":
        form_data = PostForm(request.POST, request.FILES)
        post = Post.objects.get(slug=slug)
        post.delete()
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect("front_page")
        return render(request, "blog_post/add_blog_post.html")


@login_required
def delete_blog_post(request, category_slug, slug):
    post = Post.objects.filter(slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("/")
    return redirect("/")
