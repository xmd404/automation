from twilio.rest import Client

account_sid = 'AC467d3e051109fffee1ca2a3087e659b0'
auth_token = '32ef6fc7ab25273a662362825bc47576'
client = Client(account_sid, auth_token)
twilio_number = '+12313335367'
text_this_number = '+15129869718'
message_body = 'Hey Nika... im texting you from an automated python script :) - Xavier'

message = client.messages.create(
    body=message_body,
    from_=twilio_number,
    to=text_this_number
)