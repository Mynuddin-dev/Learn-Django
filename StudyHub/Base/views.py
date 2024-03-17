from django.shortcuts import render , redirect
from django.db.models import Q
from .models import Room , Topic
from .forms import RoomForm

# ROOMS = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
#     ]

def home(request):
    # print(ROOMS)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    ROOMS = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
                                
        )
    
    topics = Topic.objects.all()
    # print(topics)

    room_count = ROOMS.count()
    context = {'ROOMS': ROOMS , 'topics': topics , 'room_count': room_count}

    return render(request, 'Base/home.html' , context)

def rooms(request , pk):

    ROOM = Room.objects.get(id=pk)   

    context = {'ROOM': ROOM}
    return render(request, 'Base/rooms.html' , context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'Base/room_form.html' , context) 

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}

    return render(request, 'Base/room_form.html' , context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'Base/delete.html' , {'obj':room})