from flask import json
from connector import create_connection


def change_password(user, password, confirmed_password, old_password):
    exists = check_existance(user)
    if len(exists) >= 1:
        temp = exists[0]
        data = temp[2]
        if old_password == data:
            user_id = get_user_id(user)
        else:
            overall_result = json.dumps({"status": "Old password is incorrect"})
            return overall_result
        if password == confirmed_password:
            update_user(str(user), str(password), user_id)

            overall_result = json.dumps({"status": "updated"})
            return overall_result
        else:
            overall_result = json.dumps({"status": "The new passwords do not match"})
            return overall_result
    else:
        overall_result = json.dumps({"status": "Username does not exist"})
        return overall_result


def get_user_id(user):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("SELECT id from Register where registerUserName = BINARY %s")
    cursor.execute(query, (user,))
    the_id = cursor.fetchone()
    result = the_id[0]
    cursor.close()
    cnx2.close()
    return result


def update_user(user, password, user_id):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Update Register set registerUserName = BINARY %s , registerUserPassword = BINARY %s where id = %s")
    cursor.execute(query, (user, password, user_id))
    cnx2.commit()
    cursor.close()
    cnx2.close()


def check_existance(user):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Register where registerUserName = BINARY %s")
    cursor.execute(query, (user,))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result
