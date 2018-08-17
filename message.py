from wunderground import *
from twilio.rest import Client
from twilioauth import *
import os


client = Client(account_sid, auth_token)

message = client.messages.create(
                              body= message,
                              from_='+12345678900',
                              to='+11234567890'
                          )

print(message.sid)



