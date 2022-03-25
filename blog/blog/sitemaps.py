from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from blog_post.models import Category
from blog_post.models import Post


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    def items(self):
        # return Post.objects.filter(status=Post.ACTIVE)
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.created_at
