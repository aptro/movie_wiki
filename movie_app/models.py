from django.db import models


class GenreMeta(models.Model):
    tag = models.CharField(max_length=127, db_index=True)


class MovieData(models.Model):
    movie_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.TextField(null=False, db_index=True)
    director = models.CharField(max_length=247, null=False)
    imdb_score = models.FloatField(default=None)
    popularity = models.FloatField(default=None)
    genre = models.ManyToManyField(GenreMeta, related_name="movies", related_query_name="movie")



