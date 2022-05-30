from django import forms
from .models import Post, User, Comment



class PostForm(forms.ModelForm):
    """ Class for making forms posts"""
    class Meta:
        model = Post
        fields = ("topic", "title", "content",)

        widgets = {
            "topic": forms.Select(attrs={'class': 'form-control'}),
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "content": forms.Textarea(attrs={'class': 'form-control'}),

        }


class CommentForm(forms.ModelForm):
    """ Class for making forms posts"""
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            "body": forms.Textarea(attrs={'class': 'form-control'}),

        }

    