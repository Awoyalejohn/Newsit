from django.urls import path
from . import views



urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),

    path('posts/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('upvote/<slug:slug>/', views.PostUpvote.as_view(), name='post_upvote'),
]