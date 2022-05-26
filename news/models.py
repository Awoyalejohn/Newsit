from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """ Topic model to create categories for posts """
    name = models.CharField(max_length=200)

    def __ste__(self):
        return self.name


class Post(models.Model):
    """ Post model to create instances of posts """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author_set')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='post_topic_set')
    last_updated = models.DateField(auto_now=True)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes_set', blank=True)

    class Meta:
        order_by = ['-created_on']

        def __str__(self):
            return self.title

        def number_of_likes(self):
            return self.likes.count()
    

    class Comment(models.Model):
        """ Comment model for comments inside posts """
        post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post_set')
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user_set')
        body = models.TextField()
        created_on = models.DateField(auto_now_add=True)

        class Meta:
            order_by = ['-created_on']
