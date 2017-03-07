from flask import Flask, render_template, request,json
from connector import create_connection


def analyse(animalIdentifier,trackingNumber,second_animalIdentifier,second_trackingNumber,user):
    x='You are in analyse'
    print(x)
    
    if animalIdentifier == '--select an animal--' and second_animalIdentifier == '--select an animal--':
        return ''
    
    locations = get_current_location(trackingNumber,second_trackingNumber)
    trackID = set()
    animals= []
    coordinates= []
    for items in locations:
        coordinates.append(items)
        coordinates.append(' ')
        
    print('coordinates')    
    print(coordinates)
    return coordinates


def get_current_location(trackingNumber,second_trackingNumber):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select currentCoordinates.longitude,currentCoordinates.latitude,Animal.animalIdentifier from currentCoordinates INNER JOIN Animal ON currentCoordinates.trackingID=Animal.trackingID where currentCoordinates.trackingID = %s or currentCoordinates.trackingID = %s")
    cursor.execute(query,(trackingNumber,second_trackingNumber))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result

