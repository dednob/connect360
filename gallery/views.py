from django.shortcuts import render
from .models import Gallery
from .serializers import GallerySerializer, GalleryReadSerializer, GallerySerializer_slider
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
        gallery = Gallery.objects.all()
        serializer = GalleryReadSerializer(gallery, many=True)
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
def gallery_detail(request, slug):
    try:
        if slug is not None:
            gallery = Gallery.objects.get(slug=slug)
            serializer = GalleryReadSerializer(gallery)
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
def gallery_by_camp(request, slug):
    try:
        gallery = Gallery.objects.filter(campaign__slug=slug)
        serializer = GallerySerializer(gallery, many=True)
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
def gallery_by_camp_slider(request, slug):
    try:
        gallery = Gallery.objects.filter(campaign__slug=slug)
        serializer = GallerySerializer_slider(gallery, many=True)
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


# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def projects_by_aow(request, pk):
#     id = pk
#     project = Projects.objects.filter(areaofwork__id = id)
#     serializer = ProjectsSerializer(project, many=True)
#     return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload(request):
    try:
        gallery_data = request.data
        if 'image' in gallery_data and gallery_data['image'] != None:
            fmt, img_str = str(gallery_data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            gallery_data['image'] = img_file

        # slug = slugify(gallery_data['title'])
        suffix = 1
        if Gallery.objects.filter(title__exact=gallery_data['title']).exists():
            count = Gallery.objects.filter(title__exact=gallery_data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(gallery_data['title']), suffix)

        else:
            slug = "%s-%s" % (slugify(gallery_data['title']), suffix)

        gallery_data['slug'] = slug

        serializer = GallerySerializer(data=gallery_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Created Data Successfully",
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
        gallery_data = request.data
        gallery = Gallery.objects.get(slug=slugkey)
        if ('image' in gallery_data and gallery_data['image'] == None) and gallery.image != None:
            gallery_data.pop('image')

        if 'image' in gallery_data and gallery_data['image'] != None:
            fmt, img_str = str(gallery_data['image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            gallery_data['image'] = img_file

        # slug = slugify(gallery_data['title'])
        suffix = 1
        if Gallery.objects.filter(title__exact=gallery_data['title']).exists():
            count = Gallery.objects.filter(title__exact=gallery_data['title']).count()
            print(count)
            suffix += count
            print("yes")
            slug = "%s-%s" % (slugify(gallery_data['title']), suffix)

        else:
            slug = "%s-%s" % (slugify(gallery_data['title']), suffix)
        gallery_data['slug'] = slug

        serializer = GallerySerializer(gallery, data=gallery_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Updated Data Successfully",
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
        project = Gallery.objects.get(slug=slug)
        project.delete()
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
