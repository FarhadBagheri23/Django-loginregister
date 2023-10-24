from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, exceptions, permissions

from . import authentication
from .serializers import CustomUserSerializer
from rest_framework.decorators import APIView
from . import services


# Create your views here.


class RegisterApiView(APIView):
    """
    Endpoint for registering new users!
    """

    def post(self,request):
        serializer = CustomUserSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)

        data = serializer.validated_data

        serializer.instance = services.create_user(user_dc = data)

        return Response({'Status':'Registered Successfully!'}, status=status.HTTP_201_CREATED)


class LoginApiView(APIView):
    """
    Endpoint for login users!
    """
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = services.filter_user_email(email= email)
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid credentials')
        
        if not user.check_password(raw_password = password):
            raise exceptions.AuthenticationFailed('Incorrect username or password!')
        

        token = services.create_token(user_id= user.id)

        response = Response()
        
        response.set_cookie(key="jwt", value = token, httponly=True)

        return response
    

class UserApiView(APIView):

    """
    This endpoint can be used when the user is authenticated!!
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    # permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)


        return Response(serializer.data)



import datetime

class TokenApiView(APIView):
    """
    This class view is for checking the generated token (Personal Use)
    """
    def get(self, request):
        token = request.COOKIES.get("jwt")
        # return Response({'token' : token})

        return Response({'message':datetime.datetime.now()})
    


class LogOutView(APIView):
    """
    This endpoint is for user Logout!
    """
    authentication_classes = [authentication.CustomUserAuthentication, ]
    permissions_classes = [permissions.IsAuthenticated, ]

    def post(self, request):

        resp = Response()
        resp.delete_cookie("jwt")
        resp.data = {'message':"Logged out!"}
        return resp