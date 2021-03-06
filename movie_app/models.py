from django.db import models
from decimal import Decimal


class GenreMeta(models.Model):
    """
    to store genre tags corresponding to each movie data
    """
    tag = models.CharField(max_length=127, db_index=True, unique=True)


class DirectorMeta(models.Model):
    """
    director for movies, one person can be director for multiple movies
    """
    name = models.CharField(max_length=247, null=False)


class MovieData(models.Model):
    """
    movie information
    """
    movie_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.TextField(null=False, db_index=True, unique=True)
    director = models.ForeignKey(DirectorMeta, related_query_name="director")
    imdb_score = models.DecimalField(default=Decimal(0), decimal_places=2, max_digits=5)
    popularity = models.DecimalField(default=Decimal(0), decimal_places=2, max_digits=15)
    genre = models.ManyToManyField(GenreMeta, related_name="movies", related_query_name="movie")

    class Meta:
        ordering = ('created_at',)



