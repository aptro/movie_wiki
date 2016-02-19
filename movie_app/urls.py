from rest_framework.routers import DefaultRouter
from .views import MovieViewSet


movie_router = DefaultRouter()
movie_router.register(r'movies', MovieViewSet, 'movie_app')
urlpatterns = movie_router.urls
