from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("add_blog_post/", views.add_blog_post, name="add_blog_post"),
    path(
        "edit_blog_post/<slug:category_slug>/<slug:slug>/",
        views.edit_blog_post,
        name="edit_blog_post",
    ),
    path(
        "delete_blog_post/<slug:category_slug>/<slug:slug>/",
        views.delete_blog_post,
        name="delete_blog_post",
    ),
    # path('search/', views.search, name='search'),
    path("<slug:category_slug>/<slug:slug>/", views.detail, name="post_detail"),
    path("<slug:slug>/", views.category, name="category_detail"),
]
