# Model Form : class based representation of a form

from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # fields = ['name', 'topic', 'description'] # Fields that we want to display in the form
        fields = '__all__' # If we want to display all the fields in the form
        exclude = ['host', 'participants'] # If we want to exclude some fields from the form