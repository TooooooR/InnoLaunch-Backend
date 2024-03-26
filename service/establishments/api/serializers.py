from django.db.models import Avg
from rest_framework import serializers
from .models import (Establishment, Comment, Amenity,
                     EstablishmentImage, Service, PriceCategory)


class EstablishmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstablishmentImage
        fields = ('image',)


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ('name', 'description')


class PriceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCategory
        fields = ('price_range',)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('id', 'establishment', 'is_active')


class EstablishmentSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True, )
    total_comments_number = serializers.SerializerMethodField(read_only=True)
    price_category = PriceCategorySerializer(read_only=True, many=True)
    url = serializers.HyperlinkedIdentityField(view_name='establishment-detail', lookup_field='slug')
    amenities = AmenitySerializer(many=True, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)
    images = EstablishmentImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Establishment
        exclude = ('slug', 'id')

    @staticmethod
    def get_total_comments_number(obj):
        return obj.comments.count()
