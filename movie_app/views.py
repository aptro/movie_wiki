from rest_framework import viewsets
from rest_framework.response import Response
from .models import MovieData
from .serializers import MovieSerializer
from django.db import transaction
from django.shortcuts import get_object_or_404
from .utils import MoviePermission, MovieFilter, MoviePaginator
from rest_framework import filters


class MovieViewSet(viewsets.GenericViewSet):
    """
    all custom or drf classes are provided as static methods so that each view type can access as attributes
    """
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [MoviePermission]
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_class = MovieFilter
    search_fields = ('name', 'director__name', 'genre__tag')
    pagination_class = MoviePaginator

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        payload = request.data
        with transaction.atomic():
            serializer = self.get_serializer(data=payload)
            if serializer.is_valid(raise_exception=True):
                serializer.save(**serializer.validated_data)
                return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        movie = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(instance=movie)
        return Response(serializer.data)

    def update(self, request, pk=None):
        payload = request.data
        serializer = self.get_serializer(instance=get_object_or_404(self.queryset, pk=pk), data=payload)
        if serializer.is_valid():
            serializer.update(serializer.instance, serializer.validated_data)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        payload = request.data
        serializer = self.get_serializer(instance=get_object_or_404(self.queryset, pk=pk), data=payload, partial=True)
        if serializer.is_valid():
            serializer.update(serializer.instance, serializer.validated_data)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        movie = get_object_or_404(self.queryset, pk=pk)
        movie.delete()
        return Response(status=204)
