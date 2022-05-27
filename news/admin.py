from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Topic, Comment

# Register your models here.
admin.site.register(Topic)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ Admin interface for posts """
    list_display = ('title', 'slug', 'topic', 'created_on', 'last_updated')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('topic', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """ Admin interface for comments """
    list_display = ('user', 'body', 'post', 'created_on')
    list_filter = ['created_on']
    search_fields = ('user', 'body')