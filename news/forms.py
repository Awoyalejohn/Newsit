from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    """ Class for making forms in Django """
    class Meta:
        model = Post
        fields = ("__all__")