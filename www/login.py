from flask import Flask,session,json
from connector import create_connection
cnx2 = create_connection()

def login(username,password,session):
    x='You are in login'
    print(x)

    if(username == '' or password == '' ):
        Result = json.dumps({"status": "Empty fields"})
        cnx2.close()
        return Result
    else:
        exists = check_existance(username)
        if(len(exists) == 1):
            temp=exists[0]
            data=temp[2]
            if(password == data[0]):
                session['user'] = username
                session['userPassword'] = password
                session['loggedIn'] = 'true'
                overallResult = json.dumps({"status": "successful"})
                cnx2.close()
                return overallResult
            else:
                overallResult = json.dumps({"status": "Incorrect Password"})
                cnx2.close()
                return overallResult
        else:
            overallResult = json.dumps({"status": "Incorrect user name"})
            cnx2.close()
            return overallResult


def check_existance(username:str):
    cursor = cnx2.cursor()
    query = ("Select * from Register where registerUserName = %s")
    cursor.execute(query,(username, ))
    result = cursor.fetchall()
    cursor.close()
    return result