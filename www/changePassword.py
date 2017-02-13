from flask import Flask, render_template, request,json
from connector import create_connection
#import mysql.connector


#cnx2 = mysql.connector.connect(host= 'gProject.mysql.pythonanywhere-services.com', user= 'gProject', password= '_mf698t_', database= 'gProject$Lamina')

def change_password(user, password, confirmedPassword, oldPassword):
    print('YURT')
    if session['loggedIn'] == False:
        if(user == '' or password == '' or confirmedPassword == '' or oldPassword == ''):
            Result = json.dumps({"status": "Empty fields"})
            print(overallResult)
            return Result
        else:
            exists = check_existance(user)
            print('exists: ' + str(len(exists)))

            if(len(exists) >= 1):
                temp=exists[0]
                data=temp[2]
                if(oldPassword == data[0]):
                     userID = get_user_id(user)
                else:
                    overallResult = json.dumps({"status": "Old password is incorrect"})
                    print(overallResult)
                    return overallResult

                if(password == confirmedPassword):

                    result = update_user(str(user), str(password),str(confirmedPassword),userID)

                    overallResult = json.dumps({"status": "updated"})
                    print(overallResult)
                    return overallResult
                else:
                    overallResult = json.dumps({"status": "The new passwords do not match"})
                    print(overallResult)
                    return overallResult


            else:
                overallResult = json.dumps({"status": "Username does not exist"})
                print(overallResult)
                return overallResult


def get_user_id(user):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("SELECT id from Register where registerUserName = %s")
    cursor.execute(query,(user,))
    theID = cursor.fetchone()
    result = theID[0]
    cursor.close()
    cnx2.close()
    return result



def update_user(user:str, password:str,confirmedPassword:str, userID):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Update Register set registerUserName = %s , registerUserPassword = %s, confirmRegisterUserPassword = %s where id = %s")
    cursor.execute(query,(user,password,confirmedPassword,userID))
    cnx2.commit()
    cursor.close()
    cnx2.close()
    return True


def check_existance(user:str):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Register where registerUserName = %s")
    cursor.execute(query,(user,))
    result = cursor.fetchall()
    print('THE RESULT IS: ' + str(result))
    cursor.close()
    cnx2.close()
    return result
