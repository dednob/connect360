from rest_framework import serializers
from .models import Areaofwork


class AreaofworkSerializer(serializers.ModelSerializer):
    # projects = ProjectsSerializer(many=True, read_only=True)
    class Meta:
        model = Areaofwork
        fields = ['id', 'title', 'details', 'slug', 'image']

class AreaofworkReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areaofwork
        fields = ['id', 'title', 'details', 'slug', 'image']

class AreaofworkCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areaofwork
        fields = ['id', 'title', 'slug']