from django.db import models
from django.utils import timezone



class ScheduledDate(models.Model):
    sh_date = models.CharField(max_length=10)

    discriptionText = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    
