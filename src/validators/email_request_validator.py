'''
Created on Oct 13, 2020

@author: dheer
'''
from src.models.requests.email_request import EmailRequest
from validator import validate
import re

class EmailRequestValidator(object):
    '''
    Validates request of type EmailRequest
    '''

    def __init__(self, params=None):
        '''
        Constructor
        '''
        self.__rules = {"emails": self.__validate_emails}
        self.__regex = r"^[a-z0-9]+[\._]?[a-z0-9\+]+[@]\w+[.]\w{2,3}$"
  
    def __validate_emails(self, emails):
        '''
        Custom validator for emails
        '''
        if emails is None or len(emails) < 1:
            return False
        validation_result = True
        for email in emails:
            validation_result = validation_result and re.search(self.__regex, email) is not None
        return validation_result
      
    def validate(self, email_request:EmailRequest):
        '''
        Validates EmailRequest
        '''
        return validate(email_request, self.__rules, return_info=True)
    
# if __name__ == '__main__':
#     email_request = EmailRequest()
#     email_request.emails = [ 'dheeraj.326@gmail.com', 'chichumail1@gmail.com' ]
#     validator = EmailRequestValidator()
#     validation_result = validator.validate(email_request.json())
#     print(validation_result.__dict__)