from flask import Flask, render_template, request,json
import mysql.connector


cnx2 = mysql.connector.connect(host= 'gProject.mysql.pythonanywhere-services.com', user= 'gProject', password= '_mf698t_', database= 'gProject$Lamina')

app = Flask(__name__)
@app.route('/currentLocation',methods=['POST','GET'])
def func3():
    x='You are in currentLocation'
    print(x)
    
    #need to join id in Tracking id in Coordinates table to id in Animal table then take the latest gps result
    
    location = get_current_location(session['user'])
    
    return location
    


def get_current_location(userID:str):
    cursor = cnx2.cursor()
    query = ("Select * from Coordinates where registerUserName = %s")
    cursor.execute(query,(username, ))
    result = cursor.fetchall()
    cursor.close()
    return result

if __name__ == "__main__":
    app.run(debug=True)