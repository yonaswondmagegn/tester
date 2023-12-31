from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class StudentMajor(models.Model):
    title = models.CharField(max_length=225)
    date  = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
    
class Group(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    sub_groups  = models.ManyToManyField('self',blank=True)
    admins = models.ManyToManyField(User,related_name='admins')
    date = models.DateTimeField(default=timezone.now)
    

    def __str__(self) -> str:
        return self.name

class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=10)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now) 


class Profile(models.Model):
    academic_year_choise = (
        ('NR','Not Registered'),
                            ('FM','FreshMan'),
                            ('SY','Second Year'),
                            ('TY','Thered Year'),
                            ('FY','Fourth Year'),
                            ('GC','Fivth Year'))
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    authority = models.CharField(max_length=225,null = True,blank=True)
    major = models.ForeignKey(StudentMajor,on_delete=models.SET_NULL,null=True,blank = True)
    image = models.ImageField(default='profile.jpg',upload_to='profile_pics')
    aastu_id_main = models.CharField(max_length=4,null=True,blank=True)
    aastu_id_year = models.CharField(max_length=2,null=True,blank=True)
    acadamic_year = models.CharField(choices=academic_year_choise,default = 'NR',max_length=2)
    bio = models.TextField(null=True,blank=True)
    group = models.ManyToManyField(Group)
    date = models.DateTimeField(default=timezone.now)


