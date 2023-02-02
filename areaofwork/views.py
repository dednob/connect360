from django.shortcuts import render
from .models import Areaofwork
from .serializers import AreaofworkSerializer, AreaofworkReadSerializer
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
def aow_list(request):
    try:
        areaofwork = Areaofwork.objects.all()
        serializer = AreaofworkReadSerializer(areaofwork, many=True)
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
def aow_detail(request, slug):
    try:
        if slug is not None:
            aow = Areaofwork.objects.get(slug=slug)
            serializer = AreaofworkSerializer(aow)
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
        aow_data = request.data
        # slug = None
        if 'image' in aow_data and aow_data['image'] != None:
            fmt, img_str = str(aow_data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            aow_data['image'] = img_file

        # slug = slugify(data['title'])
        suffix = 1
        print(aow_data['title'])
        # print(slug)

        if Areaofwork.objects.filter(title__exact=aow_data['title']).exists():
            print("yes")
            count = Areaofwork.objects.filter(title__exact=aow_data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(aow_data['title']), suffix)

        else:
            print("No")
            slug = "%s-%s" % (slugify(aow_data['title']), suffix)

        aow_data['slug'] = slug
        serializer = AreaofworkSerializer(data=aow_data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received Data Successfully",
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
            'response': "Data not Found",
            'error': str(e)
        })


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, slugkey):
    try:

        aow_data = request.data
        areaofwork = Areaofwork.objects.get(slug=slugkey)

        if ('image' in aow_data and aow_data['image']==None) and areaofwork.image!=None:
            
            aow_data.pop('image')

        if 'image' in aow_data and aow_data['image'] != None:
            fmt, img_str = str(aow_data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            aow_data['image'] = img_file

        # slug = slugify(data['title'])
        suffix = 1

        if Areaofwork.objects.filter(title__exact=aow_data['title']).exists():
            print("yes")
            count = Areaofwork.objects.filter(title__exact=aow_data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(aow_data['title']), suffix)

        else:
            slug = "%s-%s" % (slugify(aow_data['title']), suffix)

        aow_data['slug'] = slug

        
        serializer = AreaofworkSerializer(areaofwork, data=aow_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received Data Successfully",
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
            'response': "Data not Found",
            'error': str(e)
        })


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, slug):
    try:
        areaofwork = Areaofwork.objects.get(slug=slug)
        areaofwork.delete()
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
