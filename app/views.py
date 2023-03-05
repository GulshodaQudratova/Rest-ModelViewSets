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