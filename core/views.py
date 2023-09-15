from django.shortcuts import render
from .models import *


def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'core/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'core/about.html', data)


def services(request):
    return render(request, 'core/services.html')


def contact(request):
    return render(request, 'core/contact.html')
