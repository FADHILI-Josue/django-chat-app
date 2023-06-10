from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#dynamic url routing

from .models import Room

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request,pk):
    room = Room.objects.get(id=pk)

    return render(request, 'base/room.html', context)
    # return HttpResponse('room page')