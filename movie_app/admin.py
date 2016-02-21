from django.contrib import admin

from .models import MovieData, GenreMeta, DirectorMeta

admin.site.register([MovieData, GenreMeta, DirectorMeta])
