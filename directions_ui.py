#Arman Karabakhtsyan 28152667, Lab 2

import directions_api
import directions_outputs

#directions ui

def generate_navigation(locations : 'list of locations') -> 'list of Python parsed json objects':
    '''Uses Map Quest API based functions to build a list of HTTP requested json objects'''
    results = []
    for count in range(1, len(locations)):
        url = directions_api.build_url(locations[count - 1], locations[count])
        json = directions_api.get_result(url)
        if directions_api.check_status(json):
            results.append(json)
        else:
            return []
    return results

def copyright_print() -> None:
    '''Prints required MapQuest copyright message'''
    print('\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

def user_input() -> dict:
    '''Handles inputs for search and output types'''
    return {'locations' : search_data(), 'outputs' : output_data()}


def search_data() -> 'list of str locations':
    '''Get user input on locations and return a list containing them. Must be at least 2'''
    while True:
        try:
            num_locations = int(input())
            if num_locations >= 2:
                break
            print('ERROR')
        except ValueError:
            print('ERROR')
    
    locations = []
    
    for loc in range(num_locations):
        locations.append(input())

    return locations

def output_data() -> 'list of output parameters':
    '''Get user input on required outputs and return a list of Class objects of given outputs'''
    while True:
        try:
            num_outputs = int(input())
            if num_outputs >= 1 and num_outputs < 5: #max 4 unique outputs with currently implemented classes
                break
            print('ERROR')
        except ValueError:
            print('ERROR')
            
    outputs = []
    for o in range (num_outputs):   
        while True:
            par = input().upper()
            if par == 'STEPS':
                outputs.append(directions_outputs.Directions())
                break
            elif par == 'TOTALDISTANCE':
                outputs.append(directions_outputs.Distance())
                break
            elif par == 'TOTALTIME':
                outputs.append(directions_outputs.Time())
                break
            elif par == 'LATLONG':
                outputs.append(directions_outputs.LatLong())
                break
            else:
                print('ERROR')

    return outputs

def PrintNavigation(jsons : 'list of Python parsed json objects', output : list) -> None:
    '''Proceed with the requested outputs'''
    for item in output:
        directions_outputs.Output(item, jsons)
    
            
if __name__ == '__main__':
    data = user_input()
    nav_data = generate_navigation(data['locations'])
    if nav_data != []:
        PrintNavigation(nav_data, data['outputs'])
    else:
        print('ERROR')

    copyright_print()
