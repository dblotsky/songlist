from django.shortcuts import render
from setlist.models import *

def home(request):
    context = {
        'played_songs':   Song.objects.filter(played=True),
        'unplayed_songs': Song.objects.filter(played=False),
    }
    return render(request, 'home.html', context)
