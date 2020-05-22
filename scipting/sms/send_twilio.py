from twilio.rest import Client

account_sid = 'ACc460257cb578c4afdd5172fae9bf15d0'
auth_token = '146afbd4c7e51882eb322321450fc7a7'
client = Client(account_sid, auth_token)

message = client.messages.create(
            from_='+12067373018',
            body='friday yey!!!',
            to='+639657720239'
        )

print(message.sid)