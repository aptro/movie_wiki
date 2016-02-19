from rest_framework import viewsets
from rest_framework.response import Response
from .models import MovieData
from .serializers import MovieSerializer
from django.db import transaction
from django.shortcuts import get_object_or_404
from .utils import MoviePermission


class MovieViewSet(viewsets.ViewSet):
    queryset = MovieData.objects.all()
    permission_classes = [MoviePermission]

    def list(self, request):
        serializer = MovieSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        payload = request.data
        with transaction.atomic():
            serializer = MovieSerializer(data=payload)
            if serializer.is_valid(raise_exception=True):
                serializer.save(**serializer.validated_data)
                return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        movie = get_object_or_404(self.queryset, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def update(self, request, pk=None):
        payload = request.data
        serializer = MovieSerializer(instance=get_object_or_404(self.queryset, pk=pk), data=payload)
        if serializer.is_valid():
            serializer.update(serializer.instance, serializer.validated_data)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        payload = request.data
        serializer = MovieSerializer(instance=get_object_or_404(self.queryset, pk=pk), data=payload, partial=True)
        if serializer.is_valid():
            serializer.update(serializer.instance, serializer.validated_data)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        movie = get_object_or_404(self.queryset, pk=pk)
        movie.delete()
        return Response(status=204)

