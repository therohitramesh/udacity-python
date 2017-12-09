#!/usr/bin/python
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC15e97b6c3da77afa493bfd9879e62b5b"
# Your Auth Token from twilio.com/console
auth_token  = "65bbc105f88e7716471ced2e0cd8b7a1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918320486639",   #Replace with your number
    from_="+18622074641",#Replace with your Twilio number
    body="Hello there!")

print(message.sid)