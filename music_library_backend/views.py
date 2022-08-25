from django import views
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Song
from .serializers import SongSeralizer
from music_library_backend import serializers

@api_view(['GET', 'POST'])
def song_list(request):
   
   
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSeralizer(songs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SongSeralizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
            
@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = SongSeralizer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSeralizer(song, data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
