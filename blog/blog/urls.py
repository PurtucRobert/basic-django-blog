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
from core.views import robots_txt

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('about/', about_page),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('contact/', include('contact.urls')),
    path('', include('blog_post.urls')),
    path('', front_page, name='front_page'),
    path('summernote/', include('django_summernote.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
