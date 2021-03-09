from django.shortcuts import render
from .models import Project


def index(request):
    return render(request, 'portfolio/index.html')


def projects(request):
    proj = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': proj})


def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    return render(request, 'portfolio/contact.html')
