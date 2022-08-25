from itertools import product
from rest_framework import serializers
from .models import Song

class SongSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','artist','album','release_date', 'genre', 'likes']