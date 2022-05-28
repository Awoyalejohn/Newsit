from django import forms
from .models import Post, User, Comment



class PostForm(forms.ModelForm):
    """ Class for making forms posts"""
    class Meta:
        model = Post
        fields = ("topic", "title", "content",)


class CommentForm(forms.ModelForm):
    """ Class for making forms posts"""
    class Meta:
        model = Comment
        fields = ('body',)

    