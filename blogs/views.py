from django.shortcuts import render
from .models import Blog
# from events.models import Event
# from hotels.models import Hotel
# from locations.models import Location
# from reviews.models import Review
from .serializers import BlogSerializer
# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import base64
from django.core.files.base import ContentFile
from django.utils.text import slugify
from rest_framework import status


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def blog_list(request):
    try:
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many = True)
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Received data Successfully",
            'data': serializer.data

        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })

@api_view(['GET'])
def blog_list_count(request):
    try:
        blog = Blog.objects.all().count()
        print(blog)
        return Response({
            'Blog': blog

        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_blog_detail(request, slug):
    try:
        if slug is not None:
            blog = Blog.objects.get(slug=slug)
            serializer = BlogSerializer(blog)
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received data Successfully",
                'data': serializer.data

            })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    try:
        blog_data = request.data
        print(blog_data)
        if 'blog_image' in blog_data and blog_data['blog_image']!=None:
            fmt, img_str = str(blog_data['blog_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            blog_data['blog_image'] = img_file
        
        if 'banner_image' in blog_data and blog_data['banner_image']!=None:
            fmt, img_str = str(blog_data['banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            blog_data['banner_image'] = img_file
        
        # slug = slugify(blog_data['title'])
        suffix=1
        # slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
        if Blog.objects.filter(title__exact=blog_data['title']).exists():
            count=Blog.objects.filter(title__exact=blog_data['title']).count()
            print(count)
            suffix+=count
            print("yes")
            slug = "%s-%s" % (slugify(blog_data['title']), suffix)
        
        else:
            slug = "%s-%s" % (slugify(blog_data['title']), suffix)
                
        blog_data['slug']=slug

        serializer = BlogSerializer(data = blog_data, partial = True)
        if serializer.is_valid():
            serializer.save()    
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Data created successfully",
                'data': serializer.data

            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not found",
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
def update_blog(request, pk):
    try: 
        id = pk
        blog = Blog.objects.get(id = id)
        blog_data = request.data
        
        
        if ('blog_image' in blog_data and blog_data['blog_image']==None) and blog.blog_image!=None:
            
            blog_data.pop('blog_image')
        if ('banner_image' in blog_data and blog_data['banner_image']==None) and blog.banner_image!=None:
            
            blog_data.pop('banner_image')
        
        if 'blog_image' in blog_data and blog_data['blog_image']!=None:
            fmt, img_str = str(blog_data['blog_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            blog_data['blog_image'] = img_file
        
        if 'banner_image' in blog_data and blog_data['banner_image']!=None:
            fmt, img_str = str(blog_data['banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            blog_data['banner_image'] = img_file
        
        # slug = slugify(blog_data['title'])
        suffix=1
        # slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
        if Blog.objects.filter(title__exact=blog_data['title']).exists():
            count=Blog.objects.filter(title__exact=blog_data['title']).count()
            print(count)
            suffix+=count
            print("yes")
            slug = "%s-%s" % (slugify(blog_data['title']), suffix)
        
        else:
            slug = "%s-%s" % (slugify(blog_data['title']), suffix)
                
        blog_data['slug']=slug

        
        

        serializer = BlogSerializer(blog, data = blog_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Data updated successfully",
                'data': serializer.data

            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not found",
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
def delete_blog(request,pk):
    blog = Blog.objects.get(id=pk)
    try:
        blog.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Data deleted successfully",

        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


# @api_view(['GET'])
# def blog_list_count(request):
#     try:
#         blog_count = Blog.objects.all().count()
#         event_count = Event.objects.all().count()
#         review_count = Review.objects.all().count()
#         hotel_count = Hotel.objects.all().count()
#         location_count = Location.objects.all().count()
#         return Response({
#             'Response': 'Count received successfully',
#             'Blog': blog_count,
#             'Event': event_count,
#             'Review': review_count,
#             'hotel': hotel_count,
#             'location': location_count
#         })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'response': "Data not found",
#             'error': str(e)
#         })
    
    