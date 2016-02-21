import django_filters

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_text
from rest_framework import serializers
from rest_framework import permissions
from ..models import MovieData
from rest_framework import pagination
from collections import OrderedDict
from rest_framework.response import Response


class MovieSlugRelatedField(serializers.SlugRelatedField):
    default_error_messages = {
        'does_not_exist': _('Oops, {value} does not exist.'),
        'invalid': _('Invalid value.'),
    }

    def __init__(self, slug_field=None, create=False, **kwargs):
        self.create = create
        super(MovieSlugRelatedField, self).__init__(slug_field, **kwargs)

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(**{self.slug_field: data})
        except ObjectDoesNotExist:
            if self.create:
                return self.get_queryset().create(**{self.slug_field: data})
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')


class MoviePermission(permissions.BasePermission):
    SAFE_ACTIONS = ['list', 'retrieve']
    CRITICAL_ACTIONS = ['create', 'update', 'partial_update', 'destroy']
    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    def has_permission(self, request, view):
        return (request.method in self.SAFE_METHODS and request.user and request.user.is_authenticated()) or (
            request.user and request.user.is_staff)


class MovieFilter(django_filters.FilterSet):
    max_popularity = django_filters.NumberFilter(name="popularity", lookup_type="=lte")
    min_popularity = django_filters.NumberFilter(name="popularity", lookup_type="gte")
    max_imdb_score = django_filters.NumberFilter(name="imdb_score", lookup_type="lte")
    min_imdb_score = django_filters.NumberFilter(name="imdb_score", lookup_type="gte")

    class Meta:
        model = MovieData
        fields = ['max_popularity', 'min_popularity', 'max_imdb_score', 'min_imdb_score']


class MoviePaginator(pagination.PageNumberPagination):

    page_size = 10
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('has_next', self.page.has_next()),
            ('previous', self.get_previous_link()),
            ('has_previous', self.page.has_previous()),
            ('num_pages', self.page.paginator.num_pages),
            ('results', data)
        ]))