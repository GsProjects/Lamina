from flask import json
from connector import create_connection


def update_animal_details(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number, oldanimal_identifier, owner):
    if animal_identifier == '' or animal_type == '' or animal_breed == '' or animal_weight =='' or animal_gender =='' or tracking_number =='':
        Result = json.dumps({"status": "Empty fields"})
        return Result
    if animal_gender != 'M' and animal_gender != 'F' and animal_gender != 'm' and animal_gender != 'f':
            overall_result = json.dumps({"status": "Wrong gender"})
            return overall_result
    
    if animal_identifier == oldanimal_identifier  and tracking_number == oldtracking_number:
        update_animal_table(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number)
        update_coordinates_table(tracking_number, oldtracking_number)
        Result = json.dumps({"status": "Updated Successfully"})
        return Result
        
    if animal_identifier == oldanimal_identifier and tracking_number != oldtracking_number:
        associated_owners = check_id_existance(tracking_number)
        if len(associated_owners) != 0:
            for item in associated_owners:
                if item[0] == owner:
                    update_animal_table(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number)
                    update_coordinates_table(tracking_number, oldtracking_number)
                    Result = json.dumps({"status": "Updated Successfully"})
                    return Result
                else:
                    Result = json.dumps({"status": "Tracking number already in use"})
                    return Result
        else:
            update_animal_table(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number)
            update_coordinates_table(tracking_number, oldtracking_number)
            Result = json.dumps({"status": "Updated Successfully"})
            return Result
                    
    if tracking_number == oldtracking_number and animal_identifier != oldanimal_identifier:
        associated_owners = check_name_existance(animal_identifier)
        if len(associated_owners) != 0:
            for ids in associated_owners:
                if ids[0] == tracking_number:
                    update_animal_table(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number)
                    update_coordinates_table(tracking_number, oldtracking_number)
                    Result = json.dumps({"status": "Updated Successfully"})
                    return Result
                else:
                    Result = json.dumps({"status": "Animal ID associated with another animal"})
                    return Result
        else:
            update_animal_table(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number)
            update_coordinates_table(tracking_number, oldtracking_number)
            Result = json.dumps({"status": "Updated Successfully"})
            return Result
        
    if tracking_number != oldtracking_number and animal_identifier != oldanimal_identifier:
        associated_animal_names = check_name_existance(animal_identifier)
        associated_owners_ids = check_id_existance(tracking_number)
        if len(associated_animal_names) != 0 and len(associated_owners_ids) != 0:
            for ids in associated_animal_names:#each trackingID
                for item in associated_owners_ids:#each name
                    if item[0] == owner and ids[0] == tracking_number:
                        update_animal_table(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number)
                        update_coordinates_table(tracking_number, oldtracking_number)
                        Result = json.dumps({"status": "Updated Successfully"})
                        return Result
                    else:
                        if item[0] != owner:
                            Result = json.dumps({"status": "Tracking number already in use"})
                            return Result
                        if ids[0] != tracking_number:
                            Result = json.dumps({"status": "Animal ID associated with another animal"})
                            return Result
                            
        else:
            update_animal_table(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number)
            update_coordinates_table(tracking_number, oldtracking_number)
            Result = json.dumps({"status": "Updated Successfully"})
            return Result    
            

def update_animal_table(animalIdentifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Update Animal set animalIdentifier = BINARY %s,typeAnimal = BINARY %s,breedAnimal = BINARY %s,weightAnimal = %s,genderAnimal = BINARY %s,trackingID = %s where trackingID = %s")
    cursor.execute(query, (animalIdentifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number))
    cnx2.commit()
    cursor.close()
    cnx2.close()

    
def update_coordinates_table(tracking_number, oldtracking_number):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Update currentCoordinates set trackingID = %s where trackingID = %s")
    cursor.execute(query, (tracking_number, oldtracking_number))
    cnx2.commit()
    cursor.close()
    cnx2.close()

    
def check_name_existance(animalIdentifier):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select trackingID from Animal where animalIdentifier = BINARY %s")
    cursor.execute(query, (animalIdentifier,))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result
    

def check_id_existance(tracking_number):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select ownerID from Animal where trackingID = %s")
    cursor.execute(query,(tracking_number,))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result

