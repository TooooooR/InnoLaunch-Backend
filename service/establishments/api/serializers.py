from rest_framework import serializers
from service.establishments.models import Establishment, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('id', 'establishment')


class EstablishmentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='establishment-detail', lookup_field='slug')

    class Meta:
        model = Establishment
        exclude = ('slug', 'id')


class HomeSerializer(serializers.ModelSerializer):
    recommendations = EstablishmentSerializer(many=True, read_only=True)
