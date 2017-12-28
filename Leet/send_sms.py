# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
import os
from twilio.rest import Client
import logging

# # Find these values at https://twilio.com/user/account
# account_sid = "ACXXXXXXXXXXXXXXXXX"
# auth_token = "YYYYYYYYYYYYYYYYYY"
# client = TwilioRestClient(account_sid, auth_token)
#
# message = client.messages.create(to="+12316851234", from_="+15555555555",
#                                      body="Hello there!")
#
#
# .env.example
# #Twilio settings all found on dashboard
# export TWILIO_ACCOUNT_SID=ACXXXXXXXXXXXXXXXXX
# export TWILIO_AUTH_TOKEN=YYYYYYYYYYYYYY
# export TWILIO_NUMBER=+##########




class MessageClient(object):
    TWILIO_ACCOUNT_SID = ACXXXXXXXXXXXXXXXXX
    TWILIO_AUTH_TOKEN=YYYYYYYYYYYYYY
    TWILIO_NUMBER=+##########

    def __init__(self):
        (twilio_number, twilio_account_sid, twilio_auth_token) = load_twilio_config()

        self.twilio_number = twilio_number
        self.twilio_client = Client(twilio_account_sid, twilio_auth_token)

    logger = logging.getLogger(__name__)

    def load_twilio_config(self):
        twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        twilio_number = os.environ.get('TWILIO_NUMBER')

        # if not all([twilio_account_sid, twilio_auth_token, twilio_number]):
        #     logger.error(NOT_CONFIGURED_MESSAGE)
        #     raise Exception

        return (twilio_number, twilio_account_sid, twilio_auth_token)

    def send_message(self, slot_activity):
        appt_time =
        body = "Your Remedy Visit Is Confirmed for {appt_time}! " \
               "Remedy will be in touch shortly to discuss your visit. " \
               "Call 512.900.5844 if you have any questions prior to your visit." \
               "Thank you, Remedy.".format(appt_time)
        self.twilio_client.messages.create(body=body, to=appt.phone_numer, from_=self.twilio_number)
