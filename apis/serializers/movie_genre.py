from rest_framework import serializers

from movie_app.models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for Genre model
    """
    class Meta:
        model = Genre
        fields = '__all__'


class MovieDataSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model Data
    """
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('pk', 'name', 'imdb_score',
                  'popularity', 'director', 'genre')


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model
    """
    class Meta:
        model = Movie
        fields = ('name', 'imdb_score',
                  'popularity', 'director', 'genre')
