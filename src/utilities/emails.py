'''
Created on Oct 13, 2020

@author: dheer
'''
from src.data.constants import Constants

class Emails(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    
    def count_unique_emails(self, emails):
        return len(self.__cleanup_emails(emails))
    
    def __cleanup_emails(self, emails):
        '''
        Strips the emails of off irrelevant characters and 
        counts unique email addresses.
        '''
        emails = list(emails)
        print(emails)
        cleaned_emails = set()
        for email in emails:
            for character in Constants.Email.IGNORE_CHARACTERS:
                email = email.replace(character, '')
            email = email.split('@')
            email[0] = email[0].split(Constants.Email.IGNORE_AFTER)[0]
            cleaned_emails.add('@'.join(email))
        return list(cleaned_emails)
    
# emails = [
#         "dheeraj.326@gmail.com",
#         "dheeraj.326+abc@gmail.com",
#         "chichumail1@gmail.com"
#     ]
# emails_utility = Emails()
# print(emails_utility.count_unique_emails(emails))