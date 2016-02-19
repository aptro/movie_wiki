from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_text
from rest_framework import serializers


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
