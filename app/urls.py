from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('playlists',PlaylistViewSet)
router.register('musics',MusicViewSet)
urlpatterns = [
    path('',include(router.urls))
]
