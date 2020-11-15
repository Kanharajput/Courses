from django.contrib import admin
from django.urls import path
from . views import AllBlogs, DetailBlog, LikeView, DislikeView

urlpatterns = [
    path('BlogHome', AllBlogs.as_view(), name = 'blogs'),
    path('article/<int:pk>', DetailBlog.as_view(), name = 'article-detail'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    path('dislike/<int:pk>', DislikeView, name = 'dislike_post')
    ]

