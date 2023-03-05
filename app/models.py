from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class Music(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE,related_name='music')
    def __str__(self):
        return self.name
