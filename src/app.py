'''
Created on Oct 13, 2020

@author: dheer
'''
from flask import Flask
from src.models.requests.email_request import EmailRequest
from flask.globals import request
from src.validators.email_request_validator import EmailRequestValidator
from src.utilities.emails import Emails
from src.models.responses.email_response import EmailResponse
app = Flask(__name__)

@app.route('/uniqueemails', methods=['POST'])
def unique_emails():
    email_validator = EmailRequestValidator()
    email_request = EmailRequest()
    email_request.__dict__ = dict(request.json)
    validation_result, _, errors = email_validator.validate(email_request.__dict__)
    if not validation_result:
        return str(errors)
    else:
        email_utility = Emails()
        email_response = EmailResponse()
        email_response.uniqueemails = email_utility.count_unique_emails(email_request.emails)
        return email_response.json()

@app.route('/')
def hello():
    email_request = EmailRequest()
    email_request.emails = [ 'dheeraj.326@gmail.com', 'chichumail1@gmail.com' ]
    return email_request.json()

if __name__ == '__main__':
    app.run()

