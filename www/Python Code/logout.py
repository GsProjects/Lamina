from flask import Flask,session,json


def logout(session):
    if session['loggedIn'] == 'true':
        session['loggedIn'] = 'false'
        overallResult = json.dumps({"status": "You have logged out successfully"})
        return overallResult
    else:
        overallResult = json.dumps({"status": "Logout failed"})
        return overallResult