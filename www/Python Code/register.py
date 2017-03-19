from flask import Flask,json
from connector import create_connection


def register(username,password,confirmedPassword):
    if(username == '' or password == '' or confirmedPassword == ''):
        print('Yes')
        Result = json.dumps({"status": "Empty fields"})
        return Result
    else:
        exists = check_existance(username)
        if(len(exists) < 1):
            ids = get_current_id()
            add_user(str(username), str(password),str(confirmedPassword))
            overallResult = json.dumps({"status": "ok"})
            return overallResult
        else:
            overallResult = json.dumps({"status": "Username already exists"})
            return overallResult


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


def add_user(username:str, password:str,confirmedPassword:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Insert into Register (registerUserName , registerUserPassword, confirmRegisterUserPassword) values(%s, %s, %s)")
    cursor.execute(query,(username, password,confirmedPassword))
    cnx2.commit()
    cursor.close()
    cnx2.close()


def check_existance(username:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Register where registerUserName = %s")
    cursor.execute(query,(username, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result
