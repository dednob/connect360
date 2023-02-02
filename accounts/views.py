from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from rest_framework import status


# Create your views here.
@api_view(['POST'])
def RegisterView(request):
    try:
        username = request.data['username']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        group = request.data['groups']
        user = User(username=username, first_name=first_name, last_name=last_name)

        user.set_password(password)

        user.save()
        user.groups.set(group)

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                'success': 'You are authenticated',
                'user Id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'refresh': str(refresh),
                'access': str(refresh.access_token)}
        )
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not Found",
            'error': str(e)
        })

@api_view(['GET'])
def user_list(request):
    try:
        group = User.objects.all()
        serializer = UserSerializer(group, many=True)
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
