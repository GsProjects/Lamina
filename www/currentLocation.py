from flask import Flask, render_template, request,json
from connector import create_connection


def location(user):
    x='You are in currentLocation'
    print(x)

    locations = get_current_location(user)#get all locations associated with the current user
    trackID = set()
    animals= []
    coordinates= []
    for items in locations:
        trackID.add(items[1])
    
    for ids in trackID:
        animals.append( get_associated_animals(ids) )
        
    
    for animal in animals:
        for elements in animal:
            max_id = get_max_id(elements[7])
            currentlocation = get_latest_location(max_id)
            coordinates.append(currentlocation)
            coordinates.append(' ')
        
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
