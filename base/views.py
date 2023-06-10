from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#dynamic url routing

from .models import Room

rooms = [
    {'id':1, 'name': 'backend develpers'},
    {'id':2, 'name': 'font end developers'},
    {'id':3, 'name': 'fullstack developers'},
    {'id':4, 'name': 'designers'}
]

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request,pk):
    room = None

    for i in rooms:
        if i['id'] == int(pk):
            room = i
        context = {'room':room}

    return render(request, 'base/room.html', context)
    # return HttpResponse('room page')