from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer,  CategoryCampaignSerializer
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
def category_list(request):
    try:
        areaofwork = Category.objects.all()
        serializer = CategorySerializer(areaofwork, many=True)
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
def category_detail(request, slug):
    try:
        if slug is not None:
            aow = Category.objects.get(slug=slug)
            serializer = CategorySerializer(aow)
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
        cat_data = request.data
        # slug = None
        if 'image' in cat_data and cat_data['image'] != None:
            fmt, img_str = str(cat_data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            cat_data['image'] = img_file

        # slug = slugify(data['title'])
        suffix = 1
        print(cat_data['title'])
        # print(slug)

        if Category.objects.filter(title__exact=cat_data['title']).exists():
            print("yes")
            count = Category.objects.filter(title__exact=cat_data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(cat_data['title']), suffix)

        else:
            print("No")
            slug = "%s-%s" % (slugify(cat_data['title']), suffix)

        cat_data['slug'] = slug
        serializer = CategorySerializer(data=cat_data)
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

        cat_data = request.data
        category = Category.objects.get(slug=slugkey)

        if ('image' in cat_data and cat_data['image']==None) and category.image!=None:
            
            cat_data.pop('image')

        if 'image' in cat_data and cat_data['image'] != None:
            fmt, img_str = str(cat_data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            cat_data['image'] = img_file

        # slug = slugify(data['title'])
        suffix = 1

        if Category.objects.filter(title__exact=cat_data['title']).exists():
            print("yes")
            count = Category.objects.filter(title__exact=cat_data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(cat_data['title']), suffix)

        else:
            slug = "%s-%s" % (slugify(cat_data['title']), suffix)

        cat_data['slug'] = slug

        
        serializer = CategorySerializer(category, data=cat_data, partial=True)
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
def delete(request, pk):
    try:
        areaofwork = Category.objects.get(id=pk)
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
