from django.db import models
from Profile.models import Profile,Group
from django.utils import timezone

class AnouncementPost(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    title  = models.CharField(max_length=225,blank=True,null=True)
    target_group = models.ManyToManyField(Group)
    description = models.TextField(null=True,blank=True)
    date = models.DateTimeField(default=timezone.now)
