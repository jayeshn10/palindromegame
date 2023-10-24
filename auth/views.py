from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from auth.decorators import is_admin_authentication, is_self_or_admin_authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from auth.serializer import RegisterUserSerializer, UpdateUserSerializer


@api_view(['POST'])
def RegisterUser(request):
    serializers = RegisterUserSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        print(serializers.data)
        return Response(serializers.data)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def LoginUser(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
                'token': token.key
            })
    else:
        return Response({
            "error":"username or password is incorrect"
        })

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@is_self_or_admin_authentication
def UpdateUser(request, id):
    try:
        user = User.objects.get(id=id)
    except Exception as ex:
        user = None
        print(str(ex))
        return Response({
            "error":"Something went wrong"
        })
    serializers = UpdateUserSerializer(user, data=request.data)
    if serializers.is_valid():
        serializers.save()
        print(serializers.data)
        return Response(serializers.data)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@is_admin_authentication
def DeleteUser(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response({
            "message":"user deleted successfully"
        })
    except Exception as ex:
        print(str(ex))
        return Response({
            "error":"Something went wrong or user does not exists"
        },status=status.HTTP_400_BAD_REQUEST)