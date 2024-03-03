
import requests as r
from django.contrib.auth import get_user_model
User = get_user_model()


def send_push_message(title, msg):
    for user in User.objects.all():
        if user.deviceToken:
            message = {
            'to' : user.deviceToken,
            'title' : title,
            'body' : msg,
            "priority":"high"
            }
            return r.post('https://exp.host/--/api/v2/push/send', json = message)
   