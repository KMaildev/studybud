from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Python'},
    {'id': 2, 'name': 'Django'},
    {'id': 3, 'name': 'PHP'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context )


def room(request):
    return render(request, 'room.html')
