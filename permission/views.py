from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import Group
from rest_framework.response import Response
from .serializers import *
# from django.contrib.auth.decorators import login_required
from .decorator import permission_required
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import views
from rest_framework import status

# Create your views here.
# @permission_classes([IsAuthenticated])


@api_view(['GET'])
# @permission_required(['view_group'])
@permission_classes([IsAuthenticated])
def group_list(request):
    try:
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
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
# @permission_required(['add_group'])
@permission_classes([IsAuthenticated])
def create_group(request):
    try:
        name = request.data['name']
        group = Group(name=name)
        group.save()
        return Response(
            {
                'success': 'New Group Added',
                'group Id': group.id,
                'group name': group.name
            }
        )
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })

@api_view(['PATCH'])
# @permission_required(['change_group'])
@permission_classes([IsAuthenticated])
def update_group(request, slug):
    try:
        group_data = request.data
        group = Group.objects.get(slug=slug)
        serializer = GroupSerializer(group, data=group_data, partial=True)
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
# @permission_required(['delete_group'])
@permission_classes([IsAuthenticated])
def delete_blog(request, slug):
    try:
        group = Group.objects.get(slug=slug)
        group.delete()
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


# Permission view funtions

@api_view(['GET'])
def permission_list(request):
    try:
        permissions = Permission.objects.all()
        serializer = PermissionSerializer(permissions, many=True)
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
