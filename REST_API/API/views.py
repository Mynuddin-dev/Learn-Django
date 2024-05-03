from django.shortcuts import render

from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer
# Create your views here.

class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# Django REST Framework Views - Generic Views
# https://testdriven.io/blog/drf-views-part-2/#retrieveupdatedestroyapiview
