from django.shortcuts import render
from django.http import HttpResponse

from .models import Course, Artist


def home(request):
    return render(request, 'products/home.html')



def pottery_classes(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'products/pottery.html', context)



def pottery_class(request, id):
    course = Course.objects.get(id=id)
    context = {'course': course}
    return render(request, 'products/pottery_class.html', context)



def artists(request):
    artists = Artist.objects.all()
    context = {'artists': artists}
    return render(request, 'products/artists.html', context)



def artist_bio(request, id):
    artist = Artist.objects.get(id=id)
    courses = Course.objects.filter(teacher=artist)
    context = {'artist': artist, 'courses': courses}

    return render(request, 'products/artist_bio.html', context)



def account(request):
    return render(request, 'products/account.html')



def register(request):
    return render(request, 'products/register.html')


def cart(request):
    return render(request, 'products/cart.html')