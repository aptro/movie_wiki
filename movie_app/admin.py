from django.contrib import admin

from .models import MovieData, GenreMeta

admin.site.register([MovieData, GenreMeta])
