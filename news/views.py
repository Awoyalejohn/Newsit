from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.views import generic, View
from .models import Post, User
from .forms import PostForm
from django.urls import reverse



class PostList(generic.ListView):
    model = Post()
    queryset = Post.objects.all()
    template_name = 'index.html'


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        context = {"post": post}
        return render(request, "post_detail.html", context)


class PostCreate(View):
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
    











 