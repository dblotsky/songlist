from django.shortcuts import render
from setlist.models import *

def home(request):
    context = {
        'list_songs': Song.objects.filter(on_list=True),
        'other_songs': Song.objects.filter(on_list=False),
    }
    return render(request, 'home.html', context)
