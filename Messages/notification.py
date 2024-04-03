
# import requests as r
# from django.contrib.auth import get_user_model
# User = get_user_model()


# def send_push_message(title, msg):
    
#     for user in User.objects.all():
#         print(user.deviceToken,'device token ',user.phonenumber)
#         if user.deviceToken:
#             print(user,'user ...user')

#             message = {
#             'to' : user.deviceToken,
#             'title' : title,
#             'body' : msg,
#             "priority":"high"
#             }
#             try:
#                 r.post('https://exp.host/--/api/v2/push/send', json = message)
#             except:
#                 print('Error Happend on EXPO.SEND')
   

# # import aiohttp
# # from django.contrib.auth import get_user_model
# # from aiohttp import ClientSession

# # User = get_user_model()

# # async def send_push_message(title, msg):
# #     async with ClientSession() as session:
# #         for user in User.objects.all():
# #             print(user.deviceToken, 'device token ', user.phonenumber)
# #             if user.deviceToken:
# #                 print(user, 'user ...user')
# #                 message = {
# #                     'to': user.deviceToken,
# #                     'title': title,
# #                     'body': msg,
# #                     "priority": "high"
# #                 }
# #                 try:
# #                     async with session.post('https://exp.host/--/api/v2/push/send', json=message) as response:
# #                         response.raise_for_status()
# #                 except Exception as e:
# #                     print(f"Error sending push notification: {e}")



import httpx
from django.contrib.auth import get_user_model

User = get_user_model()

async def send_push_message(title, msg):
    async with httpx.AsyncClient() as client:
        for user in User.objects.all():
            print(user.deviceToken, 'device token', user.phonenumber)
            if user.deviceToken:
                print(user, 'user ...user')
                message = {
                    'to': user.deviceToken,
                    'title': title,
                    'body': msg,
                    "priority": "high"
                }
                try:
                    await client.post('https://exp.host/--/api/v2/push/send', json=message)
                except Exception as e:
                    print(f'Error happened on EXPO.SEND: {e}')

