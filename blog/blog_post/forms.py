from django import forms
from .models import Category, Comment
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostForm(forms.ModelForm):

    category = forms.ModelChoiceField(Category.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'body', 'category')
