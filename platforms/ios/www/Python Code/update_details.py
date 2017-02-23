from flask import Flask, render_template, request,json
from connector import create_connection
#TODO check that the new animal name and tracking number are not already used
#animal name and tracking number cant be associated with anyone else
#
#

def update_animal_details(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber,oldanimalIdentifier,owner):

    
    if(animalIdentifier == '' or animalType == '' or animalBreed == '' or animalWeight =='' or animalGender =='' or trackingNumber ==''):
        Result = json.dumps({"status": "Empty fields"})
        return Result
    
    if animalIdentifier == oldanimalIdentifier  and trackingNumber == oldtrackingNumber:
        update_animal_table(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber)
        update_coordinates_table(trackingNumber,oldtrackingNumber)
        Result = json.dumps({"status": "Updated Successfully"})
        return Result
        
    if animalIdentifier == oldanimalIdentifier and trackingNumber != oldtrackingNumber:
        associated_owners = check_id_existance(trackingNumber)
        if len(associated_owners) != 0:
            for item in associated_owners:
                if item[0] == owner:
                    update_animal_table(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber)
                    update_coordinates_table(trackingNumber,oldtrackingNumber)
                    Result = json.dumps({"status": "Updated Successfully"})
                    return Result
                else:
                    Result = json.dumps({"status": "Tracking number already in use"})
                    return Result
        else:
            update_animal_table(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber)
            update_coordinates_table(trackingNumber,oldtrackingNumber)
            Result = json.dumps({"status": "Updated Successfully"})
            return Result
                    
    if trackingNumber == oldtrackingNumber and animalIdentifier != oldanimalIdentifier:
        associated_owners = check_name_existance(animalIdentifier)
        if len(associated_owners) != 0:
            for ids in associated_owners:
                if ids[0] == trackingNumber:
                    update_animal_table(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber)
                    update_coordinates_table(trackingNumber,oldtrackingNumber)
                    Result = json.dumps({"status": "Updated Successfully"})
                    return Result
                else:
                    Result = json.dumps({"status": "Animal ID associated with another animal"})
                    return Result
        else:
            update_animal_table(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber)
            update_coordinates_table(trackingNumber,oldtrackingNumber)
            Result = json.dumps({"status": "Updated Successfully"})
            return Result
        
    if trackingNumber != oldtrackingNumber and animalIdentifier != oldanimalIdentifier:
        associated_animal_names = check_name_existance(animalIdentifier)
        associated_owners_ids = check_id_existance(trackingNumber)
        if len(associated_animal_names) != 0 and len(associated_owners_ids) != 0:
            for ids in associated_animal_names:#each trackingID
                for item in associated_owners_ids:#each name
                    if item[0] == owner and ids[0] == trackingNumber:
                        update_animal_table(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber)
                        update_coordinates_table(trackingNumber,oldtrackingNumber)
                        Result = json.dumps({"status": "Updated Successfully"})
                        return Result
                    else:
                        if item[0] != owner:
                            Result = json.dumps({"status": "Tracking number already in use"})
                            return Result
                        if ids[0] != trackingNumber:
                            Result = json.dumps({"status": "Animal ID associated with another animal"})
                            return Result
                            
        else:
            update_animal_table(animalIdentifier,animalType,animalBreed,animalWeight,animalGender,trackingNumber,oldtrackingNumber)
            update_coordinates_table(trackingNumber,oldtrackingNumber)
            Result = json.dumps({"status": "Updated Successfully"})
            return Result    
            
     


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

    
def check_name_existance(animalIdentifier):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select trackingID from Animal where animalIdentifier = %s")
    cursor.execute(query,(animalIdentifier,))
    result = cursor.fetchall()
    print("result" + str(result))
    print(type(result))
    cursor.close()
    cnx2.close()
    return result
    

def check_id_existance(trackingNumber):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select ownerID from Animal where trackingID = %s")
    cursor.execute(query,(trackingNumber,))
    result = cursor.fetchall()
    print("result" + str(result))
    print(type(result))
    cursor.close()
    cnx2.close()
    return result
    
    
