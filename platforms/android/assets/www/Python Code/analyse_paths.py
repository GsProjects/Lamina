from flask import json
from connector import create_connection


def analyse(animal_identifier, tracking_number, second_animal_identifier, second_tracking_number, start_date):
    if animal_identifier == '--select an animal--' or second_animal_identifier == '--select an animal--':
        return json.dumps({'status': 'No Animal Selected'})
    
    if start_date == '':
        return json.dumps({'status': 'No Date Selected'})

    locations = get_current_location(tracking_number, second_tracking_number, start_date)
    coordinates= []
    temp_list = []
    for items in locations:
        for elements in items:
            temp_list.append(str(elements))
        coordinates.append(temp_list)
        coordinates.append(' ')
        temp_list = []

    return json.dumps(coordinates)


def get_current_location(tracking_number, second_tracking_number, start_date):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select currentCoordinates.longitude,currentCoordinates.latitude,currentCoordinates.time,currentCoordinates.date,Animal.animalIdentifier from currentCoordinates INNER JOIN Animal ON currentCoordinates.trackingID=Animal.trackingID where currentCoordinates.trackingID = %s and currentCoordinates.trackingID = %s  and currentCoordinates.date >= %s")
    cursor.execute(query, (tracking_number, second_tracking_number, str(start_date)))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result

