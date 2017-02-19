from flask import Flask, render_template, request,json
from connector import create_connection
#update animal and currentCoordinate tables

def update_animal_details(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber):
    
    if(animalIdentifier == '' or animalType == '' or animalBreed == '' or animalWeight =='' or animalGender =='' or trackingNumber ==''):
        Result = json.dumps({"status": "Empty fields"})
        return Result
    
    update_animal_table(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber)
    update_coordinates_table(trackingNumber,oldtrackingNumber)
    
    return True

def update_animal_table(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Update Animal set animalIdentifier = %s,typeAnimal = %s,breedAnimal = %s,weightAnimal = %s,genderAnimal = %s,trackingID = %s where trackingID = %s")
    cursor.execute(query,(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber))
    cnx2.commit()
    cursor.close()
    cnx2.close()
    
def update_coordinates_table(trackingNumber,oldtrackingNumber):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Update currentCoordinates set trackingID = %s where trackingID = %s")
    cursor.execute(query,(trackingNumber,oldtrackingNumber))
    cnx2.commit()
    cursor.close()
    cnx2.close()
    
