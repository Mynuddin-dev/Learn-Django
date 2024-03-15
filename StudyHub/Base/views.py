from django.shortcuts import render
from .models import Room

# ROOMS = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
#     ]

def home(request):
    # print(ROOMS)
    ROOMS = Room.objects.all()
    context = {'ROOMS': ROOMS}
    return render(request, 'Base/home.html' , context)

def rooms(request , pk):
    
    ROOM = Room.objects.get(id=pk)   

    context = {'ROOM': ROOM}
    return render(request, 'Base/rooms.html' , context)
