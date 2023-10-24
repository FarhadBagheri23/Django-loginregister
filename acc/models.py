from django.db import models

# Create your models here.
from multiprocessing import Value
from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, first_name: str, last_name: str, email: str, password: str = None, is_staff= False, is_superuser=False) -> "User":
        if not email:
            raise ValueError('User must have an email!')
        if not first_name:
            raise ValueError('User must have a first name')
        if not last_name :
            raise ValueError('User must have a last name!')
        

        user = self.model(email = self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active  = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user
    

    def create_superuser(self, first_name : str, last_name:str, email:str, password:str):
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password,
            is_staff = True,
            is_superuser = True

        )

        user.save()
        return user


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length = 32, verbose_name='First name')
    last_name = models.CharField(max_length = 32, verbose_name= 'Last name')
    email = models.EmailField(verbose_name='Email', unique = True)
    password = models.CharField(max_length= 255)
    username = None


    objects = UserManager()

    USERNAME_FIELD = 'email'


    REQUIRED_FIELDS = ('first_name', 'last_name',)

    def __str__(self):
        return self.email