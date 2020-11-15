from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args = [str(pk)]))


def DislikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        post.dislikes.add(request.user)

    else:
        post.dislikes.add(request.user)

    return HttpResponseRedirect(reverse('article-detail', args = [str(pk)]))


class AllBlogs(ListView):
    model = Post
    template_name = 'blogHome.html'


class DetailBlog(DetailView):
    model = Post
    template_name = 'blogPost.html' 

    def get_context_data(self, *args, **kwargs):
        context = super(DetailBlog, self).get_context_data()  
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context
    


