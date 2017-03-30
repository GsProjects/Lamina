from flask import json
from connector import create_connection


def login(username,password):
    if username == '' or password == '':
        result = json.dumps({"status": "Empty fields"})
        return result
    else:
        exists = check_existance(username)
        if len(exists) == 1:
            temp = exists[0]
            data = temp[2]
            if password == data:
                overall_result = json.dumps({"status": "successful"})
                return overall_result
            else:
                overall_result = json.dumps({"status": "Incorrect Password"})
                return overall_result
        else:
            overall_result = json.dumps({"status": "Incorrect user name"})
            return overall_result


def check_existance(username):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Register where registerUserName = BINARY %s")
    cursor.execute(query, (username, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result
