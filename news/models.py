from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """ Post model to create instances of posts """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name=post_author)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name=post_topic)
    last_updated = models.DateField(auto_now=True)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name=post_likes, blank=True)

