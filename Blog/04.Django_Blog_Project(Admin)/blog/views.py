from django.shortcuts import render
from django.http import HttpResponse


post = [

    {
        'author': 'Md Mynuddin',
        'title': 'Blog Post1',
        'content':'First Post content',
        'date_posted': 'August 27,2022'

    },
        {
        'author': 'Md Khair',
        'title': 'Blog Post2',
        'content':'Second Post content',
        'date_posted': 'August 20,2022'

    },
        {
        'author': 'Nishad',
        'title': 'Blog Post3',
        'content':'Third Post content',
        'date_posted': 'August 23,2022'

    }

]

# Create your views here.
def home(request):
    context = {
        'posts' : post,
        'temp' : "Myn"
    }
    return render(request , 'blog/home.html' , context)

def about(request):
    return render(request , 'blog/about.html' , {'title' :'About Blog'})
