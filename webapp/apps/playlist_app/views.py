from django.shortcuts import render, redirect
from .models import Playlist

def index(request):
    playlist = Playlist.objects.first()
    context = {'playlist':playlist}
    return render(request, 'playlist_app/index.html', context)

def create(request):
    print(request.POST)
    playlist = Playlist(playlist_id=request.POST['name'])
    playlist.save()
    return redirect('/')

def edit(request, id):
    playlist = Playlist.objects.get(id=id)
    context = {'playlist':playlist}
    return render(request, 'playlist_app/edit.html', context)

def update(request, id):
    playlist = Playlist.objects.get(id=id)
    playlist.playlist_id = request.POST['name']
    playlist.save()
    return redirect('/')

def destroy(request, id):
    playlist = Playlist.objects.get(id=id)
    playlist.delete()
    return redirect('/')
