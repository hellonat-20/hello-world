import twilio
from twilio.rest import Client
import requests

account_sid = 'ACb37f64690b0cb4c9f18ebc83f37acff3'
auth_token = '402a754c80606d43b3cf16366ee4ec07'

client = Client(account_sid, auth_token)

r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()

number_iss = people['number']

message = 'Hi fun fact the number of people in space right now is' + str(number_iss)

message = client.messages.create(
    to="+919860499759",
    from_="+12183955193",
    body=Message)
print(message.sid)

