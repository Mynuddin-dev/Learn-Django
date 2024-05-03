# convert Python object into JSON object
# It will take the model and convert it into JSON Compatible format data.
from rest_framework.serializers import ModelSerializer 
from Base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'