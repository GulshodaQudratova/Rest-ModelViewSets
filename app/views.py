from django.shortcuts import render

# Create your views here.
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
# APIView - > Generic View - > ViewSet(ModelViewSet)
class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
class MusicViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user 
        user = User.objects.get(id=data['user'])
        playlist = Playlist.objects.get(id=data['playlist']) 
        music = Music.objects.create(user=user,playlist=playlist,author=data['author'],name=data['name'])
        serializer = MusicSerializer(music,partial=True,context={'request': request})
        # instance (1 ta element) - > object
        # print(data)
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    def update(self, request, *args, **kwargs):
        data = request.data 
        music_data = self.get_object() # < = > Music.objects.get(id=pk)
        music_data.name = data.get('name',music_data.name)
        music_data.author = data.get('author',music_data.author)
        if 'playlist' in data:
            playlist = Playlist.objects.get(id=data['playlist'])
            music_data.playlist = playlist
        if 'user' in data:
            user = User.objects.get(id=data['user'])
            music_data.user = user  
        music_data.save()
        # instance(get) = partial - Music.objects.get()  salom
        # queryset(filter,all) = many - Music.objects.filter()  [salom]
        serializer = MusicSerializer(music_data,partial=True,context={'request': request})  
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        music_data = self.get_object()
        music_data.delete()
        return Response({'status':'deleted'})