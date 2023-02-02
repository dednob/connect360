from rest_framework import serializers

from .models import Home


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        # fields = ['id', 'title', 'details', 'slug', 'image', 'active', 'experience_data', 'top_banner_image', 'mid_banner_image', 'mid_layer_image', 'footer_image']
        fields = '__all__'


class HomeToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['active']


class HomeExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['experience_data']
        