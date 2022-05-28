from django import forms
from .models import Post, User



class PostForm(forms.ModelForm):
    """ Class for making forms in Django """
    class Meta:
        model = Post
        fields = ("topic", "title", "content",)

    