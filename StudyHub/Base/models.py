from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here. (Create Our Database Table Here)

class User(AbstractUser):
    name = models.CharField(max_length=200 , null= True)
    email = models.EmailField(unique=True , null=True)
    bio = models.TextField(default='no bio...', max_length=300 , null=True)
    avatar = models.ImageField(null=True , default='avatar.svg')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name
    
# Django User Model : https://docs.djangoproject.com/en/5.0/ref/contrib/auth/
# Many to One Relationship : https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_one/ 
#  Many to One Relationship 
class Room(models.Model):
    host = models.ForeignKey(User , on_delete=models.SET_NULL , null=True) 
    topic = models.ForeignKey(Topic , on_delete=models.SET_NULL , null=True )
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User , related_name='participants' , blank=True)

    # updated time(when the room is updated)
    updated = models.DateTimeField(auto_now=True) 

    # created time(when the room is created)    
    created = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-updated' , '-created']
    
    def __str__(self):
        return self.name
    

class Message(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE) # Casecade means if the user is deleted then the message will also be deleted from 
    body_value = models.TextField()
    room = models.ForeignKey(Room , on_delete=models.CASCADE)
    
     # updated time(when the room is updated)
    updated = models.DateTimeField(auto_now=True) 

    # created time(when the room is created)    
    created = models.DateTimeField(auto_now_add=True) 
    class Meta:
            ordering = ['-updated' , '-created']
        
    def __str__(self):
        return self.body_value[0:50]