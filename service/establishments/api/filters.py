import django_filters
from .models import Establishment


class EstablishmentFilter(django_filters.FilterSet):
    amenities = django_filters.CharFilter(field_name='amenities__name', lookup_expr='icontains')
    services = django_filters.CharFilter(field_name='services__name', lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    type = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Establishment
        fields = ['name', 'type', 'amenities', 'services', 'recommended',
                  'address__city', 'price_category']
