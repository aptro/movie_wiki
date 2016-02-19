from rest_framework import serializers
from .models import MovieData, GenreMeta
from .utils import MovieSlugRelatedField


class MovieSerializer(serializers.ModelSerializer):
    genre = MovieSlugRelatedField(queryset=GenreMeta.objects, many=True, slug_field='tag', create=True)

    class Meta:
        model = MovieData
        fields = ('movie_id', 'name', 'director', 'imdb_score', 'popularity', 'genre')


