import re
from smtplib import SMTPDataError
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from blog_post.models import Post
from blog_post.models import Category
from core.models import Subscriber
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def front_page(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        subscriber_email = request.POST.get("sendemail", None)
        if subscriber_email:
            if Subscriber.objects.filter(email=subscriber_email):
                print(f"{subscriber_email} is already registered")
            else:
                try:
                    subscriber = Subscriber(email=subscriber_email)
                    subscriber.save()
                    send_mail(
                        "Successfully subscribed to Robo's blog",
                        "Welcome to Robo's blog",
                        subscriber_email,
                        [settings.CONTACT_EMAIL],
                    )
                except SMTPDataError:
                    return render(
                        request,
                        "core/frontpage.html",
                        {"posts": posts, "categories": categories},
                    )
    if request.method == "GET" and "category" in request.GET:
        paginator = Paginator(posts, 2)
        page = request.GET.get("page", 1)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
            value_category = Category.objects.get(title=request.GET["category"])
            posts = Post.objects.filter(category=value_category)
            return render(
                request,
                "core/frontpage.html",
                {"posts": posts, "categories": categories},
            )

    return render(
        request, "core/frontpage.html", {"posts": posts, "categories": categories}
    )


def about_page(request):
    return render(request, "core/aboutpage.html")


def robots_txt(request):
    text = [
        "User-agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
