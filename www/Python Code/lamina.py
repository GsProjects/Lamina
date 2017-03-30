from flask import Flask, request, json, session
from currentLocation import location
from register import register
from changePassword import change_password
from login import login
from logout import logout
from animalProfile import add_animal
from analyse_paths import analyse
from update_gps_config import associated_animals
from update_animal_profile import get_animal_profiles
from update_details import update_animal_details
from delete_animal import remove_profiles
from graph_movement import get_graph_details
from cluster_data import cluster
from insert_coordinates import insert_coord
import random
import hashlib


global session
app = Flask(__name__)
app.secret_key = str(random.getrandbits(256))


@app.route('/register', methods=['POST', 'GET'])
def register_user():
    global session

    temp_user = request.form['registerUserName']
    if temp_user == '' or request.form['registerUserPassword'] == '' or request.form['confirmRegisterUserPassword'] == '':
        Result = json.dumps({"status": "Empty fields"})
        return Result
    temp_password = hashlib.sha256(request.form['registerUserPassword'].encode('utf-8')).hexdigest()
    temp_confirmed_password = hashlib.sha256(request.form['confirmRegisterUserPassword'].encode('utf-8')).hexdigest()
    result = register(temp_user, temp_password, temp_confirmed_password)
    for k, v in json.loads(result).items():
        if v == 'ok':
            session['user'] = temp_user
            session['userPassword'] = temp_password
            session['loggedIn'] = 'true'
            return result
        else:
            session['user'] = ''
            session['userPassword'] = ''
            session['loggedIn'] = 'false'
            return result

    
@app.route('/changePassword', methods=['POST', 'GET'])
def change_pass():
    global session
    user = request.form['changeUserName']
    if user == '' or request.form['oldUserPassword'] == '' or request.form['changeUserPassword'] == '' or request.form['confirmChangeUserPassword'] == '':
        Result = json.dumps({"status": "Empty fields"})
        return Result
    
    old_password = hashlib.sha256(request.form['oldUserPassword'].encode('utf-8')).hexdigest()
    password = hashlib.sha256(request.form['changeUserPassword'].encode('utf-8')).hexdigest() 
    confirmed_password = hashlib.sha256(request.form['confirmChangeUserPassword'].encode('utf-8')).hexdigest()

    result = change_password(user, password, confirmed_password, old_password)
    for k, v in json.loads(result).items():
        if v == 'updated':
            session['user'] = user
            session['userPassword'] = password
            session['loggedIn'] = 'true'
            return result
        else:
            session['user'] = ''
            session['userPassword'] = ''
            session['loggedIn'] = 'false'
            return result


@app.route('/userlogin', methods=['POST', 'GET'])
def user_login():
    global session

    username = request.form['userName']
    password = hashlib.sha256(request.form['userPassword'].encode('utf-8')).hexdigest()

    result = login(username, password)
    for k, v in json.loads(result).items():
        if v == 'successful':
            session['user'] = username
            session['userPassword'] = password
            session['loggedIn'] = 'true'
            return result
        else:
            return result

        
@app.route('/animalProfile', methods=['POST', 'GET'])
def add_animals():
    global session

    animal_identifier = request.form['animalID']
    animal_type = request.form['animalType']
    animal_breed = request.form['animalBreed']
    animal_weight = request.form['animalWeight']
    animal_gender = request.form['animalGender']
    tracking_number = request.form['trackingNum']
    owner = session['user']

    if session['loggedIn'] == 'true':
        result = add_animal(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, owner)
        return result
    else:
        overall_result = json.dumps({"status": "Session timed out, please log in again"})
        return overall_result

    
@app.route('/currentLocation', methods=['POST', 'GET'])
def current_Location():

    result = location(session['user'])
    return json.dumps(result)#mysql datetime objects not json serializeable


@app.route('/analyse_paths', methods=['POST', 'GET'])
def analyse_path():

    global session
    if session['loggedIn'] == 'true':
        animal_identifier = request.form['animal']
        tracking_number = request.form['trackingNum']

        second_animal_identifier = request.form['animalTwo']
        second_tracking_number = request.form['trackingNumTwo']
        start_date = request.form['date']
        
        result = analyse(animal_identifier, tracking_number, second_animal_identifier, second_tracking_number, start_date)
        return result
        
    else:
        overall_result = json.dumps({"status": "Your session has timed out, please log in again"})
        return overall_result
        

@app.route('/logout', methods=['POST', 'GET'])
def logout_user():

    if session['loggedIn'] == 'true':
        result = logout(session)
        return result
    else:
        overall_result = json.dumps({"status": "Logout failed"})
        return overall_result
    
    
@app.route('/update_gps', methods=['POST', 'GET'])
def update_gps():

    global session
    if session['loggedIn'] == 'true':
        result = associated_animals(session['user'])
        if result != [[]]:
            return json.dumps(result)
        else:
            overall_result = json.dumps({"status": "No animals"})
            return overall_result
    else:
        overall_result = json.dumps({"status": "Your session has timed out, please log in again"})
        return overall_result
        
        
@app.route('/update_animals', methods=['POST', 'GET'])
def update_animals():

    global session
    if session['loggedIn'] == 'true':
        result = get_animal_profiles(session['user'])
        if len(result) != 0:
            return json.dumps(result)
        else:
            overall_result = json.dumps({"status": "No animals"})
            return overall_result
    else:
        overall_result = json.dumps({"status": "Your session has timed out, please log in again"})
        return overall_result
    
    
@app.route('/update_animals_details', methods=['POST', 'GET'])
def update_animal():

    global session
    print('In update animals details')
    animal_identifier = request.form['animalID']
    animal_type = request.form['animalType']
    animal_breed = request.form['animalBreed']
    animal_weight = request.form['animalWeight']
    animal_gender = request.form['animalGender']
    tracking_number = request.form['trackingNum']
    oldtracking_number = request.form['oldTrackingId']
    oldanimal_identifier = request.form['oldanimalIdentifier']

    if session['loggedIn'] == 'true':
        result = update_animal_details(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number, oldanimal_identifier, session['user'])
        return result
    else:
        overall_result = json.dumps({"status": "Your session has timed out, please log in again"})
        return overall_result
    
            
@app.route('/delete_details', methods=['POST', 'GET'])
def delete_animals():

    global session
    animal_identifier = request.form['animal']
    tracking_number = request.form['trackingNum']
    
    if session['loggedIn'] == 'true':
        result = remove_profiles(animal_identifier, tracking_number)
        return result     
    else:
        overall_result = json.dumps({"status": "Your session has timed out, please log in again"})
        return overall_result

    
@app.route('/get_animal_data', methods=['POST', 'GET'])
def animal_data():

    global session
    if session['loggedIn'] == 'true':
        result = get_graph_details(session['user'])
        print(result)
        if len(result) != 0:
            return json.dumps(result)
        else:
            overall_result = json.dumps({"status": "No animals"})
            return overall_result
    else:
        overall_result = json.dumps({"status": "Your session has timed out, please log in again"})
        return overall_result
    
    
@app.route('/get_cluster_data', methods=['POST', 'GET'])
def cluster_data():

    global session
    eps = request.form['eps']
    num_loc = request.form['num_loc']
    date = request.form['start_date']

    if session['loggedIn'] == 'true':
        result = cluster(int(eps), int(num_loc), date, session['user'])
        return json.dumps(result)   
    else:
        overall_result = json.dumps({"status": "Your session has timed out, please log in again"})
        return overall_result
    

@app.route('/insert', methods=['POST', 'GET'])
def insert_coordinates():

    global session
    payload = request.get_data()
    insert_coord(payload.decode())
    return ''

    
if __name__ == "__main__":
    app.run(debug=True)



