from flask import json
from connector import create_connection


def add_animal(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, owner):
    if animal_identifier == '' or animal_type == '' or animal_breed == '' or animal_weight == '' or animal_gender == '' or tracking_number == '':
            Result = json.dumps({"status": "Empty fields"})
            return Result
    else:
        if animal_gender != 'M' and animal_gender != 'F' and animal_gender != 'm' and animal_gender != 'f':
            overall_result = json.dumps({"status": "Wrong gender"})
            return overall_result
            
        exists = check_animal_existance(animal_identifier)
        if len(exists) <= 1:
            ids = get_current_animal_id()
            update_animal_profile(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, owner, tracking_number)
            overall_result = json.dumps({"status": "ok"})
            return overall_result
        else:
            overall_result = json.dumps({"status": "Animal id already exists"})
            return overall_result
        
        
def get_current_animal_id():
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("SELECT MAX(id) from Animal")
    cursor.execute(query)
    the_id = cursor.fetchone()
    result = the_id[0]
    cursor.close()
    cnx2.close()
    return result


def update_animal_profile(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, owner, tracking_number):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Insert into Animal (animalIdentifier , typeAnimal, breedAnimal, weightAnimal,genderAnimal,ownerID,trackingID) values(BINARY %s, BINARY %s, BINARY %s, %s, BINARY %s, BINARY %s, %s)")
    cursor.execute(query, (animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, owner, tracking_number))
    cnx2.commit()
    cursor.close()
    cnx2.close()


def check_animal_existance(animal_identifier):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Animal where animalIdentifier = BINARY %s")
    cursor.execute(query, (animal_identifier, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result