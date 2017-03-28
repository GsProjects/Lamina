from flask import json
from connector import create_connection


def remove_profiles(animal_identifier, tracking_number):
    if animal_identifier == '' or tracking_number == '':
        overall_result = json.dumps({"status": "Empty fields"})
        return overall_result
    else:
        delete_animal(tracking_number)
        delete_animal_coordinates(tracking_number)
        overall_result = json.dumps({"status": "Animal profile deleted successfully"})
        return overall_result
    
    
def delete_animal(tracking_number):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Delete from Animal where trackingID = %s")
    cursor.execute(query, (tracking_number, ))
    cnx2.commit()
    cursor.close()
    cnx2.close()
    
    
def delete_animal_coordinates(tracking_number):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Delete from currentCoordinates where trackingID = %s")
    cursor.execute(query, (tracking_number, ))
    cnx2.commit()
    cursor.close()
    cnx2.close()
