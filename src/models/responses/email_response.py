'''
Created on Oct 14, 2020

@author: dheer
'''
from src.models.base_http_model import BaseHttpModel

class EmailResponse(BaseHttpModel):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.uniqueemails = None