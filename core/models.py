from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)

        # self._meta.get_field('username').blank = True
        # self._meta.get_field('').null = True

    phonenumber = models.CharField(max_length=9)
    deviceToken = models.TextField(null = True,blank = True)