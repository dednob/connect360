from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list(request):
    try:
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
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
@permission_classes([IsAuthenticated])
def message_details(request, pk):
    try:
        contact = Contact.objects.get(id = pk)
        serializer = ContactSerializer(contact)
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
def create(request):
    try:
        data = request.data
        serializer = ContactSerializer(data=data)
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
        contact = Contact.objects.get(id=pk)
        contact.delete()
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


