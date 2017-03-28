from flask import json


def logout(session):
    if session['loggedIn'] == 'true':
        session['loggedIn'] = 'false'
        overall_result = json.dumps({"status": "You have logged out successfully"})
        return overall_result
    else:
        overall_result = json.dumps({"status": "Logout failed"})
        return overall_result
