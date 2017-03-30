from flask import json
from connector import create_connection


def register(username, password, confirmedPassword):
    exists = check_existance(username)
    if len(exists) < 1:
        if password != confirmedPassword:
            overall_result = json.dumps({"status": "Passwords incorrect"})
            return overall_result
            
        ids = get_current_id()
        add_user(str(username), str(password))
        overall_result = json.dumps({"status": "ok"})
        return overall_result
    else:
        overall_result = json.dumps({"status": "Username already exists"})
        return overall_result


def get_current_id():
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("SELECT MAX(id) from Register")
    cursor.execute(query)
    theID = cursor.fetchone()
    result = theID[0]
    cursor.close()
    cnx2.close()
    return result


def add_user(username, password):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Insert into Register (registerUserName , registerUserPassword) values(BINARY %s, BINARY %s)")
    cursor.execute(query, (username, password))
    cnx2.commit()
    cursor.close()
    cnx2.close()


def check_existance(username):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Register where registerUserName = BINARY %s")
    cursor.execute(query, (username, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result
