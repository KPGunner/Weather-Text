from wunderground import *
from twilio.rest import Client
from twilioauth import *
import os


client = Client(account_sid, auth_token)

message = client.messages.create(
                              body= message,
                              from_='+12527729034',
                              to='+12528762155'
                          )

print(message.sid)



