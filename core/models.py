from typing import Any
from django.contrib.auth.models import AbstractUser,UserManager
from django.db import models

class CustomManager(UserManager):
    def create_user(self,phonenumber,password = None,**extra_fields):
        if not phonenumber:
            return ValueError('Phone Number is Requred')
        
        user = self.model(phonenumber = phonenumber,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self,phonenumber,password = None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if not extra_fields.get('is_staff'):
            return ValueError ('Super User is_staff must be  True')
        if not extra_fields.get('is_superuser'):
            return ValueError('Super user field not checked')
        
        return self.create_user(phonenumber,password,**extra_fields)

class User(AbstractUser):
    phonenumber = models.CharField(max_length=9,unique = True)
    deviceToken = models.TextField(null = True,blank = True)
    username = models.CharField(max_length = 225,unique = False)
    objects = CustomManager()

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = []



