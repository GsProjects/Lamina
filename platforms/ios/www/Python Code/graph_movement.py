from connector import create_connection


def get_graph_details(owner):
    result = graph_data(owner)
    return result
    
    
def graph_data(owner):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Animal where ownerID = BINARY %s")
    cursor.execute(query, (owner, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result
