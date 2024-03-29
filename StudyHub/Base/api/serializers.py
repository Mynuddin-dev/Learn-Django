# convert Python object into JSON object
from rest_framework.serializers import ModelSerializer 
from Base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'