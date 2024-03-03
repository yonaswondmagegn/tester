from django.db.models.signals import post_save
from django.dispatch import receiver
from .notification import send_push_message
from .models import AnouncementPost



@receiver(post_save,sender = AnouncementPost)
def post_signal_reciever(sender,created,instance,**kwargs):
   
    send_push_message(f"{instance.title}",instance.description)
    print('hellow wome thid alkdfjlsdkfj')

