from twilio.rest import Client
accountSID = 'AC467d3e051109fffee1ca2a3087e659b0'
authToken = '32ef6fc7ab25273a662362825bc47576'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+12313335367'
myCellPhone = '+15129869718'
messageBody = 'Hey Nika... im texting you from an automated python script :) - Xavier'
message = twilioCli.messages.create(body=messageBody, from_=myTwilioNumber, to=myCellPhone)