import dataclasses

from typing import TYPE_CHECKING
from .models import CustomUser
import datetime
import jwt
from project.settings import JWT_KEY

if TYPE_CHECKING:
    from ..users.models import CustomUser

@dataclasses.dataclass
class UserDataClass:
    first_name :  str
    last_name : str
    email : str
    password : str = None
    id : int = None


    @classmethod
    def from_instance(cls, user:"CustomUser") -> "UserDataClass":
        return cls(
            first_name = CustomUser.first_name ,
            last_name = CustomUser.last_name,
            email = CustomUser.email,
            id = CustomUser.id ,
        )

def create_user(user_dc: "UserDataClass") -> "UserDataClass":
    instance = CustomUser(
        first_name = user_dc.first_name,
        last_name = user_dc.last_name,
        email = user_dc.email,  
    )

    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)


def filter_user_email(email : str) -> "CustomUser":
    user = CustomUser.objects.filter(email = email).first()

    return user


def create_token(user_id: int ) -> str:
    payload = dict(
        id = user_id,
        exp =  datetime.datetime.now() + datetime.timedelta(hours = 24),
        iat = datetime.datetime.now()
    )

    token = jwt.encode(payload = payload, key = JWT_KEY, algorithm= "HS256")
    return token


# def decode_token(token : str):
#     decoded_token = jwt.decode(token , key=JWT_KEY, algorithms=['HS256', ])
#     if decoded_token['expiry'] > datetime.datetime.utcnow():
#         pass
#     else:
#         pass   


