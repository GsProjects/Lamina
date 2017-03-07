from flask import Flask,session,json


def logout(session):
    x='You are in logout'
    print(x)
    if session['loggedIn'] == True:
        session['loggedIn'] = False
        overallResult = json.dumps({"status": "You have logged out successfully"})
        return overallResult
    else:
        overallResult = json.dumps({"status": "Logout failed"})
        return overallResult