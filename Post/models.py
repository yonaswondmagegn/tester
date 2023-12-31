from collections.abc import Iterable
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class PostFragment(models.Model):
    fragment_type = (("N",'NORMAL'),
                     ("C","CLOT"))
    title = models.CharField(max_length=20,null=True,blank=True)
    position = models.IntegerField()
    type = models.CharField(choices=fragment_type,default="N",max_length=1)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
        
    """fragments
        title
        content
        date
    """


class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    fragments = models.ManyToManyField(PostFragment,related_name="postfragment")
    view = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    # def save(self):
    #     if self.date != timezone.now:
    #         self.updated = timezone.now


class PostLike(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    un_liked = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)


class PostComment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
"""
 comment
 like
 share
"""
 
