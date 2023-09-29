from twilio.rest import Client
import os
import re

class TextConfirmation():

    def __init__(self, timer, recipient): # timer = datetime
        if not re.match(r"\+44[0-9]{10}", recipient):
            raise Exception("Not a valid phone number")
        self._recipient = recipient
        self._timer = timer
        self._order_time = timer.datetime.now()
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self._client = Client(account_sid, auth_token)
        

    def calculate_eta(self):
        return (self._order_time + self._timer.timedelta(hours=1)).strftime("%H:%M")
        
    def send(self):
        self._client.messages.create(
            to=self._recipient,
            from_= os.environ.get('TWILIO_PHONE_NUMBER'),
            body=f"Thank you! Your order was placed and will be delivered before {self.calculate_eta()}")

# Usage: 
# =====
# import datetime
# order_confirmation = OrderConfirmation(datetime, +447000000000)
# order_confirmation.send()

