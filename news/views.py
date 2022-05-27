from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


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
