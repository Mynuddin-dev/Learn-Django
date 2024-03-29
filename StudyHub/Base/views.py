from django.shortcuts import render , redirect
from django.db.models import Q
from .models import Room , Topic , Message
from .forms import RoomForm, UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# ROOMS = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
#     ]
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        # print(username , password)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user =authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect')
    
    context = {'page': page}
    return render(request, 'Base/login_register.html' , context)

def logoutUser(request):
    logout(request)
    return redirect('login')    

def registerPage(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    context = {'page': page , 'form': form}
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'Base/login_register.html' , context)

def home(request):
    # print(ROOMS)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    ROOMS = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
                                
        )
    topics = Topic.objects.all()[0:5]
    # print(topics)

    room_count = ROOMS.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q) | Q(room__name__icontains=q) | Q(user__username__icontains=q))

    context = {'ROOMS': ROOMS , 'topics': topics , 'room_count': room_count , 'room_messages': room_messages}

    return render(request, 'Base/home.html' , context)

def rooms(request , pk):

    ROOM = Room.objects.get(id=pk)   
    Room_Messages = ROOM.message_set.all() # Many to one
    participants = ROOM.participants.all() # Many to Many
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = ROOM,
            body_value = request.POST['body_value']
        )
        ROOM.participants.add(request.user)
        return redirect('rooms' , pk=ROOM.id) 

    context = {'ROOM': ROOM , 'Room_Messages': Room_Messages , 'participants': participants}
    return render(request, 'Base/rooms.html' , context)

def userProfile(request,pk):
    user = User.objects.get(id=pk)
    
    ROOMS = user.room_set.all() # All children of the user by set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    # print(topics)
    context = {'user': user , 'ROOMS': ROOMS , 'room_messages': room_messages , 'topics': topics}
    return render(request, 'Base/profile.html' , context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host = request.user,
            topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description')
        )
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     room.save()

        return redirect('home')
    
    context = {'form': form , 'topics': topics}
    return render(request, 'Base/room_form.html' , context) 


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.description = request.POST.get('description')
        room.topic = topic
        room.save()
        # form = RoomForm(request.POST, instance=room)
        # if form.is_valid():
        #     form.save()
        return redirect('home')
        
    context = {'form': form, 'topics': topics, 'room': room}

    return render(request, 'Base/room_form.html' , context)


@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'Base/delete.html' , {'obj':room})

@login_required(login_url='login')
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here!')
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'Base/delete.html' , {'obj':message})

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance= user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance= user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.id)
    return render(request, 'Base/update-user.html', {'form': form})

# @login_required(login_url='login')
def topicsPage(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'Base/topics.html', {'topics': topics})

def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'Base/activity.html' , {'room_messages': room_messages})