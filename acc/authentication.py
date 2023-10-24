from rest_framework import authentication, exceptions
import jwt

from .models import CustomUser
import time
import datetime

JWT_KEY = '410cfde423074c9e018fd189e448933ab0ee9ffba59f7e0412ca4eb7f2f81ace'


class CustomUserAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):

        current_datetime = datetime.datetime.now()
        timestamp_seconds = current_datetime.timestamp()
        timestamp_milliseconds = int(timestamp_seconds * 1000)

    

        token = request.COOKIES.get("jwt")

        if not token:
            raise exceptions.AuthenticationFailed("UN AUTHORIZED!!")
        
        payload = jwt.decode(token , key= JWT_KEY, algorithms=["HS256",])

        
        if payload:
            # if payload["exp"] >  timestamp_milliseconds:
                user = CustomUser.objects.filter(id = payload["id"]).first()
                return (user, None)
        else:
            raise exceptions.AuthenticationFailed('Invalid credentials!')

    