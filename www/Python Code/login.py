from flask import Flask,session,json
from connector import create_connection


def login(username,password):
    x='You are in login'
    print(x)
    if(username == '' or password == '' ):
        Result = json.dumps({"status": "Empty fields"})
        return Result
    else:
        exists = check_existance(username)
        if(len(exists) == 1):
            temp=exists[0]
            data=temp[2]
            if(password == data[0]):
                overallResult = json.dumps({"status": "successful"})
                return overallResult
            else:
                overallResult = json.dumps({"status": "Incorrect Password"})
                return overallResult
        else:
            overallResult = json.dumps({"status": "Incorrect user name"})
            return overallResult


def check_existance(username:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Register where registerUserName = %s")
    cursor.execute(query,(username, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result