from flask import Flask, render_template, request,json
from connector import create_connection

def insert_coord(data):
    values = data.split(' ')
    trackingId = values[0]
    names = get_names(trackingId) 
    insert_data(trackingId,values[3],values[4],values[2],values[1],names[0][0])
    
    
def get_names(trackingId):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select ownerID from Animal where trackingID = %s")
    cursor.execute(query,(trackingId, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result

def insert_data(trackingId,longitude,latitude,time,date,owner):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Insert into currentCoordinates (trackingID,longitude,latitude,time,date, username) values(%s, %s, %s,%s, %s, %s)")
    cursor.execute(query,(trackingId,longitude,latitude,time,date,str(owner)))
    cnx2.commit()
    cursor.close()
    cnx2.close()

