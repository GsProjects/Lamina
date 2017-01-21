from flask import Flask, render_template, request,json
import mysql.connector


cnx2 = mysql.connector.connect(host= 'gProject.mysql.pythonanywhere-services.com', user= 'gProject', password= '_mf698t_', database= 'gProject$Lamina')

app = Flask(__name__)
app.secret_key = 'b\x808\xa7\x84\x1e\xfc\x96\xc0\xbf\xb1\x80>\x97c**I\xb1\xaf\x94U\xaaz\xbb
'
@app.route('/register',methods=['POST','GET'])
def func():
    x='You are in register'
    print(x)

    tempUser = request.form['registerUserName']
    tempPassword = request.form['registerUserPassword']
    tempConfirmedPassword = request.form['confirmRegisterUserPassword']


    username = tempUser.lower()
    password = tempPassword.lower()
    confirmedPassword = tempConfirmedPassword.lower()


    if(username == '' or password == '' or confirmedPassword == ''):
        Result = json.dumps({"status": "Empty fields"})
        return Result
    else:
        exists = check_existance(username)
        if(len(exists) == 1):
            ids = get_current_id()

            result = add_user(str(username), str(password),str(confirmedPassword))

            overallResult = json.dumps({"status": "ok"})
            return overallResult
        else:
            overallResult = json.dumps({"status": "Username already exists"})
            return overallResult


def get_current_id():
    cursor = cnx2.cursor()
    query = ("SELECT MAX(id) from Register")
    cursor.execute(query)
    theID = cursor.fetchone()
    result = theID[0]
    cursor.close()
    return result



def add_user(username:str, password:str,confirmedPassword:str):
    cursor = cnx2.cursor()
    query = ("Insert into Register (registerUserName , registerUserPassword, confirmRegisterUserPassword) values(%s, %s, %s)")
    cursor.execute(query,(username, password,confirmedPassword))
    cnx2.commit()
    cursor.close()
    return True


def check_existance(username:str):
    cursor = cnx2.cursor()
    query = ("Select * from Register where registerUserName = %s")
    cursor.execute(query,(username, ))
    result = cursor.fetchall()
    cursor.close()
    return result
    
@app.route('/changePassword',methods=['POST','GET'])
def func2():
    x='You are in change password'
    print(x)

    tempUser = request.form['changeUserName']
    tempOldPassword = request.form['oldUserPassword']
    tempPassword = request.form['changeUserPassword']
    tempConfirmedPassword = request.form['confirmChangeUserPassword']


    user = tempUser.lower()
    oldPassword = tempOldPassword.lower()
    password = tempPassword.lower()
    confirmedPassword = tempConfirmedPassword.lower()


    if(user == '' or password == '' or confirmedPassword == '' or oldPassword == ''):
        Result = json.dumps({"status": "Empty fields"})
        return Result
    else:
        exists = check_existance(user)

        if(len(exists) == 1):
            temp=exists[0]
            data=temp[2]
            if(oldPassword == data[0]):
                 userID = get_user_id(user)
            else:
                overallResult = json.dumps({"status": "Old password is incorrect"})
                return overallResult

            if(password == confirmedPassword):

                result = update_user(str(user), str(password),str(confirmedPassword),userID)

                overallResult = json.dumps({"status": "updated"})
                return overallResult
            else:
                overallResult = json.dumps({"status": "The new passwords do not match"})
                return overallResult


        else:
            overallResult = json.dumps({"status": "Username does not exist"})
            return overallResult


def get_user_id(user):
    cursor = cnx2.cursor()
    query = ("SELECT id from Register where registerUserName = %s")
    cursor.execute(query,(user,))
    theID = cursor.fetchone()
    result = theID[0]
    cursor.close()
    return result



def update_user(user:str, password:str,confirmedPassword:str, userID):
    cursor = cnx2.cursor()
    query = ("Update Register set registerUserName = %s , registerUserPassword = %s, confirmRegisterUserPassword = %s where id = %s")
    cursor.execute(query,(user,password,confirmedPassword,userID))
    cnx2.commit()
    cursor.close()
    return True


def check_existance(user:str):
    cursor = cnx2.cursor()
    query = ("Select * from Register where registerUserName = %s")
    cursor.execute(query,(user,))
    result = cursor.fetchall()
    cursor.close()
    return result
    
@app.route('/userlogin',methods=['POST','GET'])
def func():
    x='You are in login'
    print(x)

     tempUser = request.form['userName']
    tempPassword = request.form['userPassword']
    


    username = tempUser.lower()
    password = tempPassword.lower()
    
    if(username == '' or password == '' ):
        Result = json.dumps({"status": "Empty fields"})
        return Result
    else:
        exists = check_existance(username)
        if(len(exists) == 1):
            temp=exists[0]
            data=temp[2]
            if(oldPassword == data[0]):
                overallResult = json.dumps({"status": "successful"})
                return overallResult
            else:
                overallResult = json.dumps({"status": "Incorrect Password"})
                return overallResult
        else:
            overallResult = json.dumps({"status": "Incorrect user name"})
            return overallResult


def check_existance(username:str):
    cursor = cnx2.cursor()
    query = ("Select * from Register where registerUserName = %s")
    cursor.execute(query,(username, ))
    result = cursor.fetchall()
    cursor.close()
    return result



if __name__ == "__main__":
    app.run(debug=True)