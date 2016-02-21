from rest_framework import serializers
from .models import MovieData, GenreMeta, DirectorMeta
from .utils import MovieSlugRelatedField


class MovieSerializer(serializers.ModelSerializer):
    genre = MovieSlugRelatedField(queryset=GenreMeta.objects, many=True, slug_field='tag', create=True)
    director = MovieSlugRelatedField(queryset=DirectorMeta.objects, slug_field='name', create=True)

    class Meta:
        model = MovieData
        fields = ('movie_id', 'name', 'director', 'imdb_score', 'popularity', 'genre')


