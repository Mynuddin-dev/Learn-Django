from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostList.as_view(), name='blogpost-view-creat'),
    path('blogposts/<int:pk>/', views.BlogPostRetriveUpdateDestroy.as_view(), name='blogpost-detail'),
]