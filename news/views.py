from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.views import generic, View
from .models import Post
from .forms import PostForm



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
        post = Post.objects.all()

        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            post_form.instance.name = request.user.username
            post_form.save()
        else:
            post_form = PostForm()
        
        context = {"post": post, "post_form": PostForm()}
        return render(request, "post_create.html", context)
    











 