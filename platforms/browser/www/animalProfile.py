from flask import Flask, render_template, request,json
import mysql.connector


cnx2 = mysql.connector.connect(host= 'gProject.mysql.pythonanywhere-services.com', user= 'gProject', password= '_mf698t_', database= 'gProject$Lamina')

app = Flask(__name__)
@app.route('/animalProfile',methods=['POST','GET'])
def func4():
    x='You are in animalProfile'
    print(x)
    
    #TODO if the tracking id entered is already associated with another user then prompt them to enter another one so a user cant track other peoples pets/animals to get a rough approximation of their location
    

    tempAnimalIdentifier = request.form['animalID']
    tempType= request.form['animalType']
    tempBreed = request.form['animalBreed']
    tempWeight = request.form['animalWeight']
    tempGender= request.form['animalGender']


    animalIdentifier = tempAnimalIdentifier.lower()
    animalType = tempType.lower()
    animalBreed = tempBreed.lower()
    animalWeight = tempWeight.lower()
    animalGender = tempGender.lower()
    owner = session['user']

    print("THE SESSION USERNAME IS : " + owner)


    if(animalIdentifier == '' or animalType == '' or animalBreed == '' or animalWeight =='' or animalGender ==''):
        Result = json.dumps({"status": "Empty fields"})
        return Result
    else:
        exists = check_animal_existance(animalIdentifier)
        if(len(exists) <= 1):
            ids = get_current_id()

            #TODO get owner id and add to argument list
            result = update_animal_profile(animalIdentifier, animalType,animalBreed, animalWeight, animalGender,owner)

            overallResult = json.dumps({"status": "ok"})
            return overallResult
        else:
            overallResult = json.dumps({"status": "Animal id already exists"})
            return overallResult


def get_current_id():
    cursor = cnx2.cursor()
    query = ("SELECT MAX(id) from Animal")
    cursor.execute(query)
    theID = cursor.fetchone()
    result = theID[0]
    cursor.close()
    return result


#TODO change update_animal_profile argument list
def update_animal_profile(animalIdentifier, animalType,animalBreed, animalWeight, animalGender,owner):
    cursor = cnx2.cursor()
    query = ("Insert into Animal (animalIdentifier , typeAnimal, breedAnimal, weightAnimal,genderAnimal,ownerID) values(%s, %s, %s,%s, %s, %s)")
    cursor.execute(query,(animalIdentifier, animalType,animalBreed, animalWeight, animalGender,owner))
    cnx2.commit()
    cursor.close()
    return True

#TODO parameter list
def check_animal_existance(animalIdentifier:str):
    cursor = cnx2.cursor()
    query = ("Select * from Animal where animalIdentifier = %s")
    cursor.execute(query,(animalIdentifier, ))
    result = cursor.fetchall()
    cursor.close()
    return result


if __name__ == "__main__":
    app.run(debug=True)