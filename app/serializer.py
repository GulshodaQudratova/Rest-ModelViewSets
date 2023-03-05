from rest_framework import serializers
from .models import *
# related_name orqali boglangan class ni malumotlarini olish
# 1-usul  -  tavsiya qilinmaydi
# class PlaylistSerializer(serializers.ModelSerializer):
#     musics = serializers.StringRelatedField(many=True,read_only=True)
#     class Meta:
#         model = Playlist
#         fields = '__all__'
#         read_only_fields = ['id']
#         # depth,exclude
class MusicSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ['id','url']
# 2-usul  -- bu usul qulay
class PlaylistSerializer(serializers.ModelSerializer):
    # musics = MusicSerializer(many=True,read_only=True)
    music = serializers.HyperlinkedIdentityField(view_name='musics-detail',many=True)
    class Meta:
        model = Playlist
        fields = '__all__'
        read_only_fields = ['id','url']
        # depth,exclude