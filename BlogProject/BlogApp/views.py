from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'BlogApp/home.html' , context)

class PostListView(ListView):
    model = Post
    template_name = 'BlogApp/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    

class PostDetailView(DetailView):
    model = Post
   

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'BlogApp/about.html' , context) 