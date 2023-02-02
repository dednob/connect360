from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    # projects = ProjectsSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'title', 'details', 'slug', 'image']

# class AreaofworkReadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Areaofwork
#         fields = ['id', 'title', 'details', 'slug', 'image']

class CategoryCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']