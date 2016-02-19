from rest_framework import viewsets
from rest_framework.response import Response
from .models import MovieData
from .serializers import MovieSerializer
from django.db import transaction


class MovieViewSet(viewsets.ViewSet):
    authentication_classes = ()

    def list(self, request):
        queryset = MovieData.objects.all()
        serializer = MovieSerializer(queryset, many=True)
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
        return Response(data={'test': 1232})

    def update(self, request, pk=None):
        return Response(data={'test': 1232})

    def partial_update(self, request, pk=None):
        return Response(data={'test': 1232})

    def destroy(self, request, pk=None):
        return Response(data={'test': 1232})
