from connector import create_connection


def check_flag(username):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select isLoggedIn from Register where registerUserName = BINARY %s")
    cursor.execute(query, (username, ))
    result = cursor.fetchone()
    cursor.close()
    cnx2.close()
    return result[0]
  
  
def is_logged_in(username):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Update Register set isLoggedIn = 1  where registerUserName = BINARY %s")
    cursor.execute(query, (username, ))
    cnx2.commit()
    cursor.close()
    cnx2.close()
 
    
    
def is_logged_out(username):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Update Register set isLoggedIn = 0  where registerUserName = BINARY %s")
    cursor.execute(query, (username, ))
    cnx2.commit()
    cursor.close()
    cnx2.close()
   