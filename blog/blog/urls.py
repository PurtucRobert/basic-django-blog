from django.contrib import admin
from django.urls import path
from django.urls import include
from .sitemaps import CategorySitemap
from .sitemaps import PostSitemap
from core.views import front_page
from core.views import about_page
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('about/', about_page),
    path('', include('blog_post.urls')),
    path('', front_page)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
