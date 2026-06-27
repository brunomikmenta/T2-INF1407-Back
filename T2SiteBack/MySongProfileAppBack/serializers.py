from rest_framework import serializers
from .models import Song, User

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['username', 'email', 'senha']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['username', 'firstName', 'lastName', 'gender', 'email']


class SongSerializer(serializers.ModelSerializer):

    class Meta:

        model = Song
        fields = ['id', 'name', 'artist', 'gender']