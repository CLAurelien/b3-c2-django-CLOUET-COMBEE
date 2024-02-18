from django.shortcuts import render, redirect
from .models import Sites
from .forms import SiteForm
from django.http import HttpResponse



def index(request):
    return render(request, 'index.html')


def list(request):
    sites = Sites.objects.all()
    return render(request, 'liste_sites.html', {'sites': sites})


def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save()
            return redirect('/list')
    else:
        form = SiteForm()

    return render(request, 'add_site.html', {'form': form})

def edit_site(request, id):
    site = Sites.objects.get(id=id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('/list')
    else:
        form = SiteForm(instance=site)

    return render(request, 'edit_site.html', {'form': form})