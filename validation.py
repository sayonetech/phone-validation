import csv
import json

# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest.lookups import TwilioLookupsClient
from twilio.rest.exceptions import TwilioRestException

# Your Account Sid and Auth Token from twilio.com/user/account
# Store them in the environment variables:
# "TWILIO_ACCOUNT_SID" and "TWILIO_AUTH_TOKEN"
# client = TwilioLookupsClient()
client = TwilioLookupsClient(account='Your Account ID',
                             token='Your secret token')


def is_valid_number(number):
    try:
        response = client.phone_numbers.get(number, include_carrier_info=True)
        response.phone_number  # If invalid, throws an exception.
        with open('valid_phone_no.csv', 'a') as fv:
            w = csv.DictWriter(fv, row.keys())
            w.writerow(row)
        return True
    except TwilioRestException as e:
        if e.code == 20404:
            return False
        else:
            raise e


class Validator:
    def get_phone_no(self, row):
        phone_no = row['phone_no']
        return phone_no


val = Validator()

with open('input.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        phone_no = val.get_phone_no(row)
        val.is_valid_number(phone_no)

