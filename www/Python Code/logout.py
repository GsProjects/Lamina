from flask import Flask,session,json


def logout(session):
    if session['loggedIn'] == True:
        session['loggedIn'] = False
        overallResult = json.dumps({"status": "You have logged out successfully"})
        return overallResult
    else:
        overallResult = json.dumps({"status": "Logout failed"})
        return overallResult