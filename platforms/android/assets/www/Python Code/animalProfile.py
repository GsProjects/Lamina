from flask import Flask,json
from connector import create_connection


def add_animal(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,owner):
    if(animalIdentifier == '' or animalType == '' or animalBreed == '' or animalWeight =='' or animalGender =='' or trackingNumber ==''):
            Result = json.dumps({"status": "Empty fields"})
            return Result
    else:
        exists = check_animal_existance(animalIdentifier)
        if(len(exists) <= 1):
            ids = get_current_animal_id()

            result = update_animal_profile(animalIdentifier, animalType,animalBreed, animalWeight, animalGender,owner,trackingNumber)

            overallResult = json.dumps({"status": "ok"})
            return overallResult
        else:
            overallResult = json.dumps({"status": "Animal id already exists"})
            return overallResult
        
        
def get_current_animal_id():
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("SELECT MAX(id) from Animal")
    cursor.execute(query)
    theID = cursor.fetchone()
    result = theID[0]
    cursor.close()
    cnx2.close()
    return result


def update_animal_profile(animalIdentifier, animalType,animalBreed, animalWeight, animalGender,owner,trackingNumber):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Insert into Animal (animalIdentifier , typeAnimal, breedAnimal, weightAnimal,genderAnimal,ownerID,trackingID) values(%s,%s, %s, %s,%s, %s, %s)")
    cursor.execute(query,(animalIdentifier, animalType,animalBreed, animalWeight, animalGender,owner,trackingNumber))
    cnx2.commit()
    cursor.close()
    cnx2.close()
    return True


def check_animal_existance(animalIdentifier:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Animal where animalIdentifier = %s")
    cursor.execute(query,(animalIdentifier, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result