from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.views.generic import (
    ListView ,
    DetailView , 
    CreateView ,
    UpdateView ,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'BlogApp/home.html' , context)

class PostListView(ListView):
    model = Post
    template_name = 'BlogApp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'BlogApp/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
   
class PostCreateView(LoginRequiredMixin , CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

   
class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin , UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'BlogApp/post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return messages.warning(self.request , 'You are not allowed to update this post!')

class PostDeleteView(LoginRequiredMixin ,UserPassesTestMixin , DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return messages.warning(self.request , 'You are not allowed to update this post!')

   


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'BlogApp/about.html' , context) 



"""
PostDetailView (Detail View):
    By default, DetailView looks for a template with the name
        <app>/<model>_detail.html.

In your case, since the model is Post and the app is BlogApp, Django will look for a template named 
        BlogApp/post_detail.html.

If you want to specify a different template, you can set the template_name attribute in the view.

PostCreateView (Create View):
    By default, CreateView looks for a template with the name
        <app>/<model>_form.html.

In your case, since the model is Post and the app is BlogApp, Django will look for a template named
        BlogApp/post_form.html.


This template typically contains a form for creating a new Post object.
If you want to specify a different template or customize the form rendering, you can set the template_name attribute in the view.

"""