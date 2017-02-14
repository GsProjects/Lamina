from flask import Flask, render_template, request,json
from connector import create_connection


def location(user):
    x='You are in currentLocation'
    print(x)

    #need to join id in Tracking id in Coordinates table to id in Animal table then take the latest gps result
    locations = get_current_location(user)#get all locations associated with the current user
    trackID = set()
    animals= []
    coordinates= []
    for items in locations:
            trackID.add(items)
            animals = get_associated_animals(trackID)
    
    print('Animals: ' + str(animals))

    for animal in animals:
        max_id = get_max_id(animal[7])
        currentlocation = get_latest_location(max_id)
        coordinates.append(currentlocation)
    #get max id for each animal tracking id

    return coordinates
   

def get_max_id(trackingID):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("SELECT MAX(id) from currentCoordinates where trackingID = %s")
    cursor.execute(query,(trackingID, ))
    theID = cursor.fetchone()
    result = theID[0]
    cursor.close()
    cnx2.close()
    return result


def get_latest_location(max_id):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("SELECT currentCoordinates.longitude,currentCoordinates.latitude, Animal.animalIdentifier from currentCoordinates INNER JOIN Animal ON currentCoordinates.trackingID=Animal.trackingID where currentCoordinates.id = %s")
    cursor.execute(query,(max_id, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result


def get_current_location(userID:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from currentCoordinates where username = %s")
    cursor.execute(query,(userID, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result

def get_associated_animals(trackID):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Animal where trackingID = %s")
    cursor.execute(query,(trackID, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result
