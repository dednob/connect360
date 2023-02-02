from rest_framework import serializers
from campaign.serializers import *
from .models import Gallery

from campaign.models import *

class GallerySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Gallery
        fields = '__all__'


class GalleryReadSerializer(serializers.ModelSerializer):
    
    campaign = serializers.SerializerMethodField('camp_title', read_only=True)

    def camp_title(self, obj):
        campaign_instance = Campaigns.objects.get(id = obj.campaign.id)
        return CampaignsGallerySerializer(campaign_instance).data
    
    class Meta:
        model = Gallery
        fields = '__all__'


class GallerySerializer_slider(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['image']
