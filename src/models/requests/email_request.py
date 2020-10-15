'''
Created on Oct 13, 2020

@author: dheer
'''
from src.models.base_http_model import BaseHttpModel

class EmailRequest(BaseHttpModel):
    '''
    List of emails to be checked for unique ones
    '''


    def __init__(self, params=None):
        '''
        Constructor
        '''
        self.emails = []
        
# if __name__ == '__main__':
#     email_request = EmailRequest()
#     email_request.emails = [ 'dheeraj.326@gmail.com', 'chichumail1@gmail.com' ]
#     print(email_request.to_json())