from django.shortcuts import render, get_object_or_404, redirect
from  django.db.models import Q
from django.views.generic import ListView
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm
from .models import Post, User, Comment, Topic



class PostList(View):

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q') if request.GET.get('q') != None else ''

        posts = Post.objects.filter(
            Q(topic__name__icontains=q) |
            Q(author__username__icontains=q) |
            Q(title__icontains=q)
            )
        topics = Topic.objects.all()


        context = {"posts": posts, "topics": topics}
        return render(request, "index.html", context)





class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comment_post_set.all()
        comment_form = CommentForm()
        
        context = {"post": post, "comments": comments, "comment_form": comment_form}
        return render(request, "post_detail.html", context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comment_form = CommentForm(request.POST)
        comment_form.instance.user = request.user
        comment_form.instance.post = post
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect(self.request.path_info)




class PostCreate(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        form = PostForm()
        context = {'form': form}
        return render(request, "post_create.html", context)

    def post(self, request, *args, **kwargs):

        form = PostForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    











 