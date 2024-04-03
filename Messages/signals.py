# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .notification import send_push_message
# from .models import AnouncementPost



# @receiver(post_save,sender = AnouncementPost)
# def post_signal_reciever(sender,created,instance,**kwargs):
   
#     send_push_message(f"{instance.title}",instance.description)


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AnouncementPost
from .notification import send_push_message
import asyncio


@receiver(post_save, sender=AnouncementPost)
async def post_signal_receiver(sender, created, instance, **kwargs):
    asyncio.run(send_push_message(f"{instance.title}", instance.description))
