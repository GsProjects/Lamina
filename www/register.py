from flask import Flask, render_template, request,json
from connector import create_connection
#import mysql.connector


#cnx2 = mysql.connector.connect(host= 'gProject.mysql.pythonanywhere-services.com', user= 'gProject', password= '_mf698t_', database= 'gProject$Lamina')

def register(username,password,confirmedPassword,session):
    x='You are in register'
    print(x)
    if session['loggedIn'] == False:
        if(username == '' or password == '' or confirmedPassword == ''):
            Result = json.dumps({"status": "Empty fields"})
            return Result
        else:
            exists = check_existance(username)
            if(len(exists) <= 1):
                ids = get_current_id()

                result = add_user(str(username), str(password),str(confirmedPassword))

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
    return True


def check_existance(username:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Register where registerUserName = %s")
    cursor.execute(query,(username, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result
