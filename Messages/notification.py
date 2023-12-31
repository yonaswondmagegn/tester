from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
import requests as r
import os
import requests
import rollbar

# Optionally providing an access token within a session if you have enabled push security
session = requests.Session()
session.headers.update(
    {
        "Authorization": "Bearer 736be085eacd29c1503eb22c35489e4d",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "content-type": "application/json",
    }
)

# Basic arguments. You should extend this function with the push features you
# want to use, or simply pass in a `PushMessage` object.
def send_push_message(token,title, message):
    message = {
    'to' : token,
    'title' : title,
    'body' : message,
    "priority":"high"
    }
    return r.post('https://exp.host/--/api/v2/push/send', json = message)
    # try:
    #     response = PushClient(session=session).publish(
    #         PushMessage(to=token, body=message, data=extra)
    #     )
    #     print(response)
    # except DeviceNotRegisteredError:
    #     print(f"Device with token {token} is not registered.")
    # except PushServerError as e:
    #     print(f"Error from the push server: {e.errors}")
    # except PushTicketError as e:
    #     print(f"Error from Expo's push ticket system: {e.push_response._asdict()}")
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")
