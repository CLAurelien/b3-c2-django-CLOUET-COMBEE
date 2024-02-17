from django.shortcuts import render
from .models import Sites
from django.http import HttpResponse


def index(request):
    sites = Sites.objects.all()
    return render(request, 'liste_sites.html', {'sites': sites})
