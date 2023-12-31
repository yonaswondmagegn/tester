from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save,sender = User)
def create_profile(sender,created,instance,**kwargs):
    if created:
        Profile.objects.create(user = instance,aastu_id_main = instance.username[:4],aastu_id_year = instance.username[5:])
