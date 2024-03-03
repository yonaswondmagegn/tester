from django.shortcuts import render
from .models import ScheduledDate
from .serializer import ScheduledDateSerializer
from rest_framework.viewsets import ModelViewSet



class ScheduledDateViewSet(ModelViewSet):
    queryset = ScheduledDate.objects.all()
    serializer_class = ScheduledDateSerializer
    
