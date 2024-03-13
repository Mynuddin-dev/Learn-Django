from django.shortcuts import render

ROOMS = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
    ]

def home(request):
    # print(ROOMS)
    context = {'ROOMS': ROOMS}
    return render(request, 'Base/home.html' , context)

def rooms(request , pk):
    print(pk)
    ROOM =None
    for i in ROOMS:
        if i['id'] == int(pk):
            ROOM = i
            
    context = {'ROOM': ROOM}
    return render(request, 'Base/rooms.html' , context)
