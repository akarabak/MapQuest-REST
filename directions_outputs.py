#Arman Karabakhtsyan 28152667, Lab 2

#This module contains different output classes

def Output(outClassObject, jsons : 'list of Python parsed json objects') -> None:
    '''Uses generate methods on class '''
    print(outClassObject.generate(jsons))


class LatLong:   
    def generate(self, jsons):
        '''Returns latitude and longtitude in proper str formatting'''
        result = ''
        for json in jsons:
            for routes in json['route']['locations']:
                lat = routes['latLng']['lat']
                long = routes['latLng']['lng']

                if lat < 0 and long < 0:
                    result += ('\n{:.2f}S {:.2f}W'.format(abs(lat), abs(long)))
                elif lat > 0 and long < 0:
                    result += ('\n{:.2f}N {:.2f}W'.format(abs(lat), abs(long)))
                elif lat < 0 and long > 0:
                    result += ('\n{:.2f}S {:.2f}E'.format(abs(lat), abs(long)))
                elif lat > 0 and long > 0:
                    result += ('\n{:.2f}N {:.2f}E'.format(abs(lat), abs(long)))
        return result
    
class Distance:
    def __init__(self):
        '''Initializes a Distance with a distance of zero'''
        self._distance = 0
    def generate(self, jsons):
        '''Returns total distance'''
        for json in jsons:
            self._distance += json['route']['distance']
        return ('\nTotal Distance: {:.0f} miles').format(self._distance)

class Time:
    def __init__(self):
        '''Initializes a Time with a time of zero'''
        self._time = 0
    def generate(self, jsons):
        '''Returns total time'''
        for json in jsons:
            self._time += json['route']['time'] // 60 #in minutes
        return ('\nTotal Time: ' + str(self._time) + ' minutes')

class Directions:
    '''Initializes a Direction with first line of str to be DIRECTIONS'''
    def __init__(self):
        self._directions = '\nDIRECTIONS'
    def generate(self, jsons):
        for json in jsons:
            for routes in json['route']['legs']:
                for directions in routes['maneuvers']:
                    self._directions += '\n' + directions['narrative']
        return self._directions
