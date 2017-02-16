from flask import Flask, render_template, request,json
from connector import create_connection


def analyse(user):
    x='You are in analyse'
    print(x)

    locations = get_current_location(user)#get all locations associated with the current user
    trackID = set()
    animals= []
    coordinates= []
    for items in locations:
        coordinates.append(items)
        coordinates.append(' ')
    
    print('THE COORDINATES ARE:' + str(coordinates))
    return coordinates


def get_current_location(userID:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select longitude,latitude from currentCoordinates where username = %s")
    cursor.execute(query,(userID, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result

