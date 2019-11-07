from django.shortcuts import render, redirect
from app.models import Album, Song


def album(request, id):
    item = Album.objects.get(id=id)
    album = Album.objects.create(title=song.title, artist_name=album.artist_name)
    item.save()
    return redirect("album_list")


def album_list(request):
    return album_list.html

def new_song(request):
    
