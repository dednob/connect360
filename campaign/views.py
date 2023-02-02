from django.shortcuts import render
from .models import Campaigns
from .serializers import CampaignsSerializer, CampaignsListSerializer, CampaignsPostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.text import slugify
import base64
from django.core.files.base import ContentFile
from rest_framework import status


# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def list(request):
    try:
        campaigns = Campaigns.objects.all()
        serializer = CampaignsListSerializer(campaigns, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Received Data Successfully",
            "data": serializer.data
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })


@api_view(['GET'])
def campaign_detail(request, slug):
    try:
        if slug is not None:
            campaigns = Campaigns.objects.get(slug=slug)
            serializer = CampaignsSerializer(campaigns)
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received Data Successfully",
                "data": serializer.data
            })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def campaigns_by_projects(request, slug):
    try:
        campaigns = Campaigns.objects.filter(projects__slug=slug)
        serializer = CampaignsSerializer(campaigns, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Received Data Successfully",
            "data": serializer.data
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def related_by_projects(request, slug, pk):
    try:
        campaigns = Campaigns.objects.filter(projects__slug=slug).exclude(id=pk)
        serializer = CampaignsSerializer(campaigns, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Received Data Successfully",
            "data": serializer.data
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    try:
        campaign_data = request.data
        if 'image' in campaign_data and campaign_data['image'] != None:
            fmt, img_str = str(campaign_data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            campaign_data['image'] = img_file

            # slug = slugify(campaign_data['title'])
            suffix = 1
            if Campaigns.objects.filter(title__exact=campaign_data['title']).exists():
                count = Campaigns.objects.filter(title__exact=campaign_data['title']).count()
                print(count)
                suffix += count
                print("yes")
                slug = "%s-%s" % (slugify(campaign_data['title']), suffix)

            else:
                slug = "%s-%s" % (slugify(campaign_data['title']), suffix)

            campaign_data['slug'] = slug
            serializer = CampaignsPostSerializer(data=campaign_data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Data Created Successfully",
                    "data": serializer.data
                })
            else:
                return Response({
                    'code': status.HTTP_400_BAD_REQUEST,
                    'response': "Data not Valid",
                    'error': serializer.errors
                })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })
   

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, slugkey):
    try:
        campaign_data = request.data
        campaign = Campaigns.objects.get(slug=slugkey)

        if ('image' in campaign_data and campaign_data['image']==None) and campaign.image!=None:
            
            campaign_data.pop('image')

        if 'image' in campaign_data and campaign_data['image'] != None:
            fmt, img_str = str(campaign_data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            campaign_data['image'] = img_file

            # slug = slugify(campaign_data['title'])
            suffix = 1
            if Campaigns.objects.filter(title__exact=campaign_data['title']).exists():
                count = Campaigns.objects.filter(title__exact=campaign_data['title']).count()
                print(count)
                suffix += count
                print("yes")
                slug = "%s-%s" % (slugify(campaign_data['title']), suffix)

            else:
                slug = "%s-%s" % (slugify(campaign_data['title']), suffix)

        campaign_data['slug'] = slug

        
        serializer = CampaignsSerializer(campaign, data=campaign_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Data Updated Successfully",
                    "data": serializer.data
                })
        else:
            return Response({
                    'code': status.HTTP_400_BAD_REQUEST,
                    'response': "Data not Valid",
                    'error': serializer.errors
                })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, slug):
    try:
        campaign = Campaigns.objects.get(slug=slug)
        campaign.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Data Deleted"
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })
