from re import search
from django.contrib import admin
from .models import Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin


class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body', 'title', 'intro', )
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'intro', 'category', 'body']
    list_filter = ['category', 'created_at']
    inlines = [CommentItemInline]


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title', )}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'body']
    list_filter = ['email', 'created_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
