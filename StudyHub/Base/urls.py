from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    
    path('', views.home, name='home'),
    path('rooms/<str:pk>/', views.rooms, name='rooms'),
    
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
]