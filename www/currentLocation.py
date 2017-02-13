from flask import Flask, render_template, request,json
import mysql.connector


cnx2 = mysql.connector.connect(host= 'gProject.mysql.pythonanywhere-services.com', user= 'gProject', password= '_mf698t_', database= 'gProject$Lamina')

def location(user):
    x='You are in currentLocation'
    print(x)

    #need to join id in Tracking id in Coordinates table to id in Animal table then take the latest gps result
    locations = get_current_location(user)
    trackID = set()
    animals= []
    coordinates= []
    for items in locations:
            trackID = items[1]
            animals = get_associated_animals(trackID)

    for animal in animals:
        max_id = get_max_id(animal[7])
        currentlocation = get_latest_location(max_id)
        coordinates.append(currentlocation)
        print('BEFORE JSON' + str(coordinates))
    #get max id for each animal tracking id

    print('just befor return ' + str(coordinates))
    return coordinates
    #r =json.dumps(coordinates)
    #print(r)

    #return  json.dumps(coordinates)#mysql datetime objects not json serializeable

def get_max_id(trackingID):
    cursor = cnx2.cursor()
    query = ("SELECT MAX(id) from currentCoordinates where trackingID = %s")
    cursor.execute(query,(trackingID, ))
    theID = cursor.fetchone()
    result = theID[0]
    cursor.close()
    return result


def get_latest_location(max_id):
    cursor = cnx2.cursor()
    query = ("SELECT trackingID,longitude,latitude,username from currentCoordinates where id = %s")
    cursor.execute(query,(max_id, ))
    result = cursor.fetchall()
    cursor.close()
    return result


def get_current_location(userID:str):
    cursor = cnx2.cursor()
    query = ("Select * from currentCoordinates where username = %s")
    cursor.execute(query,(userID, ))
    result = cursor.fetchall()
    cursor.close()
    return result

def get_associated_animals(trackID):
    cursor = cnx2.cursor()
    query = ("Select * from Animal where trackingID = %s")
    cursor.execute(query,(trackID, ))
    result = cursor.fetchall()
    cursor.close()
    return result
