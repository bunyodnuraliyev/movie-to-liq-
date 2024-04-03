from rest_framework import serializers
from .models import Actor, Movie, Comment


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'birthdate', 'id']

    def validate_name(self, value):
        if value[0].islower():
            raise serializers.ValidationError("ismni bosh harfini katta harf bilan kiriting")
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("raqam kiritmang harf kiriting iltimos ")
        return value

    def validate_birthdate(self, value):
        if value.year > 2005:
            raise serializers.ValidationError("xato 2005 dan katta yil yozing")
        return value


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'year', 'actor', 'id']

    def validate_birth(self, value):
        if value.year < 1930:
            raise serializers.ValidationError("Chop etilgan yili 1930 dan katta bulsin")
        return value


class CommentSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['user_id', 'movie_id', 'content']
