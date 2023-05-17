from django.forms import ModelForm
from django import forms
from .models import Post
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
