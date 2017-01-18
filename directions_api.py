#Arman Karabakhtsyan 28152667, Lab 2

import urllib.request
import urllib.parse
import json

#API handler

KEY = 'Fmjtd%7Cluu821u2nl%2Crs%3Do5-94axhu'
BASE_URL = 'http://open.mapquestapi.com/directions/v2'

def build_url(address1, address2) -> str:
    '''Build and return a request URL with given query parameters'''
    query_parameters = [('from', address1), ('to', address2)]

    return BASE_URL + '/route?key=' + KEY + '&' + urllib.parse.urlencode(query_parameters)
                        

def get_result(url) -> 'Python parsed json objects':
    '''Returns server response in python readable format if connection was successful, and empty dict otherwise'''
    response = None
    json_object = {}
    try:    
        response = urllib.request.urlopen(url)
        json_object = json.loads(response.read().decode(encoding = 'utf-8'))
    finally:
        if response != None:
            response.close()
        return json_object
            
    
    
    
def check_status(json) -> bool:
    '''Function returs False if server has no response on given input'''
    if json == {}:
        return False
    return json['info']['statuscode'] == 0
