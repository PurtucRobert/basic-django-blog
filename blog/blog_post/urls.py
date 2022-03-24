from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category_slug>/<slug:slug>/',
         views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail')
]
