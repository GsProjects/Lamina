from flask import Flask,json
from connector import create_connection


def associated_animals(owner):
    animal_data =[]
    animals = associated_animal_info(owner)
    
    for items in animals:
        animal_data.append(items)
        animal_data.append(' ')
    
    return animal_data
    
    
def associated_animal_info(owner:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select animalIdentifier, trackingID from Animal where ownerID = %s")
    cursor.execute(query,(owner, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result
    
    
