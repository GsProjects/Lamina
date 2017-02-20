from flask import Flask,json
from connector import create_connection
def remove_profiles(animalIdentifier, trackingNumber,owner):
    
    if animalIdentifier =='' or trackingNumber == '':
        overallResult = json.dumps({"status": "Empty fields"})
        return overallResult
    
    delete_animal(trackingNumber)
    delete_animal_coordinates(trackingNumber)
    return True
    
    
def delete_animal(trackingNumber:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Delete from Animal where trackingID = %s")
    cursor.execute(query,(trackingNumber, ))
    cnx2.commit()
    cursor.close()
    cnx2.close()
    
def delete_animal_coordinates(trackingNumber:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Delete from currentCoordinates where trackingID = %s")
    cursor.execute(query,(trackingNumber, ))
    cnx2.commit()
    cursor.close()
    cnx2.close()