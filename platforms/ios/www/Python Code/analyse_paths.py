from flask import Flask,json
from connector import create_connection
import datetime


def analyse(animalIdentifier,trackingNumber,second_animalIdentifier,second_trackingNumber,start_date):
    if animalIdentifier == '--select an animal--' or second_animalIdentifier == '--select an animal--':
        return json.dumps({'status':'No Animal Selected'})
    
    if start_date == '':
        return json.dumps({'status':'No Date Selected'})

    locations = get_current_location(trackingNumber,second_trackingNumber,start_date)
    coordinates= []
    temp_list =[]
    for items in locations:
        for elements in items:
            temp_list.append(str(elements))
        coordinates.append(temp_list)
        coordinates.append(' ')
        temp_list =[]

    return json.dumps(coordinates)


def get_current_location(trackingNumber,second_trackingNumber,start_date):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select currentCoordinates.longitude,currentCoordinates.latitude,currentCoordinates.time,currentCoordinates.date,Animal.animalIdentifier from currentCoordinates INNER JOIN Animal ON currentCoordinates.trackingID=Animal.trackingID where currentCoordinates.trackingID = %s and currentCoordinates.trackingID = %s  and currentCoordinates.date >= %s")
    cursor.execute(query,(trackingNumber,second_trackingNumber,str(start_date)))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result

