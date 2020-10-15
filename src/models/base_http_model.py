'''
Created on Oct 13, 2020

@author: dheer
'''
import json
from flask import jsonify

class BaseHttpModel(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    def json(self):
        return jsonify(self.__dict__)
    

    