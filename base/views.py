from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .forms import RoomForm
# Create your views here.
#dynamic url routing

from .models import Room, Topic

# rooms= [
#     {'id': 1, 'name': 'lets learn dj'},
#     {'id': 2, 'name': 'lets learn djago'},
#     {'id': 3, 'name': 'lets learn html'},
# ]

# ---------------- sign-IN page ---------------------

def loginPage(request):
    context ={'page':'sign-in'}
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exists!')
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else :
            messages.error(request, 'username or password does not exists' )
    return render(request, 'base/login_register.html', context)

# ---------------- sign-OUT page ---------------------

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

# ---------------- sign-UP page ---------------------

def registerUser(request):
    form = UserCreationForm()
    
    context ={'form':form}
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error('something went wrong!!')
            
    return render(request, 'base/login_register.html', context)


# ---------------- GET ROOMS (HOME) page ---------------------

def home(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    topics = Topic.objects.all()
    rooms_number = rooms.count()
    context = {'rooms': rooms, 'topics': topics,'rooms_nbr':rooms_number}
    return render(request, 'base/home.html', context)
    # return render(request, 'home.html', {'rooms': rooms})

# ---------------- GET ROOM page ---------------------

def room(request,pk):
    room = None
    room = Room.objects.get(id=pk)
    
    # for i in rooms:
    #     if(i['id'] == int(pk)):
    #         room = i
    context = {'room': room}

    return render(request, 'base/room.html', context)
    # return render(request, 'room.html', context)
    # return HttpResponse('room page')

# ---------------- CREATE ROOM page ---------------------

@login_required(login_url='loginPage')
def createRoom(request):
    form = RoomForm()
    if  request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form }
    return render(request, 'base/room_form.html', context)

# ---------------- UPDATE ROOM page ---------------------

@login_required(login_url='loginPage')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse('you are not allowed to perfom action to others rooms')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form }
    return render(request, 'base/room_form.html', context)


# ---------------- delete room page ---------------------

@login_required(login_url='loginPage')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj': room.name }
    return render(request, 'base/delete.html', context)