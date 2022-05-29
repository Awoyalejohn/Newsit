from django.shortcuts import render, get_object_or_404, redirect, reverse
from  django.db.models import Q
from django.views.generic import ListView, UpdateView
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm
from .models import Post, User, Comment, Topic
from django.template.defaultfilters import slugify
from django.contrib import messages



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
        number_of_comments = comments.count()
        comment_form = CommentForm()
        upvoted = False
        if post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        
        context = {"post": post, "comments": comments, "comment_form": comment_form, "upvoted": upvoted, 'number_of_comments': number_of_comments}
        return render(request, "post_detail.html", context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comment_form = CommentForm(request.POST)
        comment_form.instance.user = request.user
        comment_form.instance.post = post
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, 'Comment was successful')
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
            messages.success(request, 'Post was created successfuly')
            return redirect(reverse('home'))
    


class PostUpvote(LoginRequiredMixin, View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.upvotes.filter(id=request.user.id).exists():
            post.upvotes.remove(request.user)
        else:
            post.upvotes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))




class PostUpdate(LoginRequiredMixin, View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        form = PostForm(instance=post)
        context = {'post': post,'form': form}
        return render(request, "post_update.html", context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            post.slug = slugify(form.instance.title)
            post.save()
            messages.success(request, 'Post was updated successfully')
            return redirect(reverse('home'))


class PostDelete(LoginRequiredMixin, View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        context = {'post': post}
        return render(request, "post_delete.html", context)
        
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        post.delete()
        messages.success(request, 'Post was deleted successfully')
        return redirect(reverse('home'))



class CommentUpdate(LoginRequiredMixin, View):

    def get(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        comment_form = CommentForm(instance=comment)
        
        context = {'comment_form': comment_form}
        return render(request, "comment_update.html", context)

    def post(self, request, slug, comment_id, *args, **kwargs):
        post_slug = get_object_or_404(Post, slug=slug)
        slug = post_slug.slug
        comment = get_object_or_404(Comment, id=comment_id)
        comment_form = CommentForm(request.POST, instance=comment)
        
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, 'Updated comment successfully')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CommentDelete(LoginRequiredMixin, View):
    def get(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        context = {'comment': comment}
        return render(request, "comment_delete.html", context)

    def post(self, request, slug, comment_id, *args, **kwargs):
        post_slug = get_object_or_404(Post, slug=slug)
        slug = post_slug.slug
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        messages.success(request, 'Comment has been deleted')
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))



class Profile(View):
    def get(self, request, pk, *args, **kwargs):
        user = User.objects.get(id=pk)
        posts = user.post_author_set.all()
        comments = user.comment_user_set.all()


        context = {'user': user, 'posts': posts, 'comments': comments}
        return render(request, 'profile.html', context)

