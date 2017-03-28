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


global session
app = Flask(__name__)
app.secret_key = str(random.getrandbits(256))


@app.route('/register', methods=['POST', 'GET'])
def register_user():
    global session

    temp_user = request.form['registerUserName'].lower()
    temp_password = request.form['registerUserPassword'].lower()
    temp_confirmed_password = request.form['confirmRegisterUserPassword'].lower()
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
def change_password():
    global session

    user = request.form['changeUserName'].lower()
    old_password = request.form['oldUserPassword'].lower()
    password = request.form['changeUserPassword'].lower()
    confirmed_password = request.form['confirmChangeUserPassword'].lower()

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

    username = request.form['userName'].lower()
    password = request.form['userPassword'].lower()

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
def add_animal():
    global session

    animal_identifier = request.form['animalID'].lower()
    animal_type = request.form['animalType'].lower()
    animal_breed = request.form['animalBreed'].lower()
    animal_weight = request.form['animalWeight'].lower()
    animal_gender = request.form['animalGender'].lower()
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
def analyse_paths():

    global session
    if session['loggedIn'] == 'true':
        animal_identifier = request.form['animal'].lower()
        tracking_number = request.form['trackingNum']

        second_animal_identifier = request.form['animalTwo'].lower()
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
def update_animal_details():

    global session
    print('In update animals details')
    animal_identifier = request.form['animalID'].lower()
    animal_type = request.form['animalType'].lower()
    animal_breed = request.form['animalBreed'].lower()
    animal_weight = request.form['animalWeight'].lower()
    animal_gender = request.form['animalGender'].lower()
    tracking_number = request.form['trackingNum']
    oldtracking_number = request.form['oldTrackingId']
    oldanimal_identifier = request.form['oldanimalIdentifier'].lower()

    if session['loggedIn'] == 'true':
        result = update_animal_details(animal_identifier, animal_type, animal_breed, animal_weight, animal_gender, tracking_number, oldtracking_number, oldanimal_identifier, session['user'])
        return result
    else:
        overall_result = json.dumps({"status": "Your session has timed out, please log in again"})
        return overall_result
    
            
@app.route('/delete_details', methods=['POST', 'GET'])
def delete_animal():

    global session
    animal_identifier = request.form['animal'].lower()
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



