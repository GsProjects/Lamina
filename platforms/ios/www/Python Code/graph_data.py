from flask import Flask,json
from connector import create_connection
def graph_info(animalIdentifier, trackingNumber,owner):
    newresult=[]
    
    if animalIdentifier =='--select an animal--' or trackingNumber == '':
        overallResult = json.dumps({"status": "Empty fields"})
        return overallResult
    else:
        result = animal_graph_data(trackingNumber)
        for items in result:
            newresult.append(str(items))
        return newresult
    
    
def animal_graph_data(trackingNumber:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select longitude,latitude,time from currentCoordinates where trackingID = %s")
    cursor.execute(query,(trackingNumber, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result
