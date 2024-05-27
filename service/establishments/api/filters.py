import django_filters
from .models import Establishment


class EstablishmentFilter(django_filters.FilterSet):
    amenities = django_filters.CharFilter(method='filter_amenities')
    services = django_filters.CharFilter(method='filter_services')
    type = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Establishment
        fields = ['type', 'amenities', 'services', 'is_recommended', 'price_category', 'capacity']

    def filter_amenities(self, queryset, name, value):
        amenities_list = value.split(';')
        queryset = queryset
        for amenity in amenities_list:
            queryset = queryset.filter(amenities__name__icontains=amenity)
        return queryset

    def filter_services(self, queryset, name, value):
        services_list = value.split(';')
        queryset = queryset
        for amenity in services_list:
            queryset = queryset.filter(services__name__icontains=amenity)
        return queryset
