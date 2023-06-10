from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#dynamic url routing


courses = [
    {'id':1, 'name': 'js'},
    {'id':2, 'name': 'python'},
    {'id':3, 'name': 'ruby'},
    {'id':4, 'name': 'react'}
]

def home(request):
    return render(request, 'base/home.html', {'courses': courses})

def room(request,pk):
    course = None

    for i in courses:
        if i['id'] == int(pk):
            course = i
        context = {'course':course}

    return render(request, 'base/room.html', context)
    # return HttpResponse('room page')