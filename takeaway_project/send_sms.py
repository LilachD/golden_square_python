from twilio.rest import Client


account_sid = "y"
auth_token  = "x"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+447000000000",
    from_="+447000000001",
    body="Hello!")

print(message.sid)

