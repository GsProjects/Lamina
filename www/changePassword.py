from flask import Flask, render_template, request,json
import mysql.connector


cnx2 = mysql.connector.connect(host= 'gProject.mysql.pythonanywhere-services.com', user= 'gProject', password= '_mf698t_', database= 'gProject$Lamina')

app = Flask(__name__)
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



if __name__ == "__main__":
    app.run(debug=True)