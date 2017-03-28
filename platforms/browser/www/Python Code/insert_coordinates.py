from connector import create_connection


def insert_coord(data):
    values = data.split(' ')
    tracking_id = values[0]
    names = get_names(tracking_id)
    insert_data(tracking_id, values[3], values[4], values[2], values[1], names[0][0])
    
    
def get_names(tracking_id):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select ownerID from Animal where trackingID = %s")
    cursor.execute(query, (tracking_id, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result


def insert_data(tracking_id, longitude, latitude, time, date, owner):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Insert into currentCoordinates (trackingID,longitude,latitude,time,date, username) values(%s, %s, %s,%s, %s, %s)")
    cursor.execute(query, (tracking_id, longitude, latitude, time, date, str(owner)))
    cnx2.commit()
    cursor.close()
    cnx2.close()

