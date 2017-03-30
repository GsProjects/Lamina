from connector import create_connection


def location(user):
    locations = get_current_location(user)#get all locations associated with the current user
    track_id = set()
    animals= []
    coordinates= []
    for items in locations:
        track_id.add(items[1])
    
    for ids in track_id:
        animals.append(get_associated_animals(ids))
        
    for animal in animals:
        for elements in animal:
            max_id = get_max_id(elements[7])
            currentlocation = get_latest_location(max_id)
            for items in currentlocation:
                for elements in items:
                    coordinates.append(str(elements))
            coordinates.append(' ')

    return coordinates
   

def get_max_id(tracking_id):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("SELECT MAX(id) from currentCoordinates where trackingID = %s")
    cursor.execute(query, (tracking_id, ))
    the_id = cursor.fetchone()
    result = the_id[0]
    cursor.close()
    cnx2.close()
    return result


def get_latest_location(max_id):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("SELECT currentCoordinates.longitude,currentCoordinates.latitude,currentCoordinates.time,currentCoordinates.date, Animal.animalIdentifier from currentCoordinates INNER JOIN Animal ON currentCoordinates.trackingID=Animal.trackingID where currentCoordinates.id = %s")
    cursor.execute(query, (max_id, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result


def get_current_location(user_id):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from currentCoordinates where username = BINARY %s")
    cursor.execute(query, (user_id, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result


def get_associated_animals(track_id):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select * from Animal where trackingID = %s")
    cursor.execute(query, (track_id, ))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result
