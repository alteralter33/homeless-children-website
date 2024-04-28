from django.shortcuts import render

from .models import Kid123
from .models import Country123

def home(request):
    country = Country123.objects.all()
    return render(request, 'Group18MissingKids.html', {'Country123': country})

def country(request, id):
    country = Country123.objects.get(id=id)
    kids = country.kid.all()
    return render(request, 'country.html', {'kid': kids})

def details(request, id):
    kid = Kid123.objects.get(id=id)
    return render(request, 'details.html', {'kid': kid})




