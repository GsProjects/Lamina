from flask import Flask, render_template, request,json
import mysql.connector


cnx2 = mysql.connector.connect(host= 'gProject.mysql.pythonanywhere-services.com', user= 'gProject', password= '_mf698t_', database= 'gProject$Lamina')

app = Flask(__name__)
@app.route('/userlogin',methods=['POST','GET'])
def func3():
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
        print("CONTENTS Exists :" + str(exists))
        if(len(exists) == 1):
            temp=exists[0]
            data=temp[2]
            print("CONTENTS DATA[0] :" + str(data))
            if(password == data[0]):
                session['user'] = username
                session['userPassword'] = password
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