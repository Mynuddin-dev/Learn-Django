# Django form for user registration
# for add more fields in UserCreationForm 

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

## inherit from UserCreationForm and add email field

class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField() ## add email field to UserCreationForm

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# This is not custom user model , if we just want to add more fields in UserCreationForm then we have to create custom user form.
# For custom user model we normally use AbstractUser model in models.py file and that was(User) not under Authentication, Authorization and User Management section in admin panel.