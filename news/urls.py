from django.urls import path
from . import views



urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/update/<slug:slug>/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/delete/<slug:slug>/', views.PostDelete.as_view(), name='post_delete'),

    path('posts/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('upvote/<slug:slug>/', views.PostUpvote.as_view(), name='post_upvote'),
    path('posts/<slug:slug>/<comment_id>/comment_update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('posts/<slug:slug>/<comment_id>/comment_delete/', views.CommentDelete.as_view(), name='comment_delete'),
    path('profile/<str:pk>/', views.Profile.as_view(), name='profile'),
]