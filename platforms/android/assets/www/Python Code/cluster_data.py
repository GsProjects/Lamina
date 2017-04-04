from flask import json
from connector import create_connection
import numpy as np
from sklearn.cluster import DBSCAN
from collections import defaultdict


def cluster(distance, num_locations, date, end_date, user):
    coordinate_data = []
    cluster_data = []
    animal_ids = get_associated_animals(user)
    for animal in animal_ids:

        #http://geoffboeing.com/2014/08/clustering-to-reduce-spatial-data-set-size/   
        if distance == '' or num_locations == '' or date == '' or end_date == '':
            overall_result = {"status": "Empty Fields"}
            return overall_result
        
        if animal[0] != '':
            data = get_coordinates(animal[0], date,end_date)
            
        if date == end_date:
            return {'status': 'Same Dates'}
        
        if date > end_date:
            return {'status': 'Date order'}
        
        if len(data) <= 1:
            overall_result = {"status": "No Data"}
            return overall_result

        kms_per_radian = 6371.0088
        value = float(distance)/1000
        eps = value/kms_per_radian
        coordinates = []
        temp_data = []
        for elements in data:
            for items in elements:
                temp_data.append(float(items))
            coordinates.append(temp_data)
            temp_data = []

        coords = np.matrix(coordinates)
        #min_samples =1 means every point get assigned to a cluster or becomes a cluster itself
        #ball_tree algorithm hyper spheres multidimensional each point belongs to one sphere only
        #ball_tree partition data into nested spheres, more costly than kd tree more efficient multidimensional
        db = DBSCAN(eps, min_samples=int(num_locations), algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
        #kmeans requires you to specify the number of clusters in advance which dbscan doesnt it uses eps and min_samples
   
        cluster_labels = db.labels_
        #core samples:  A point is a core point if it has more than a specified number of points (MinPts) within Eps—These are points that are at the interior of a cluster.

        temp = []
        for i, element in enumerate(cluster_labels):
            coordinate = data[i]
            temp.append((str(element), [coordinate[0], coordinate[1]]))

        d = defaultdict(list)
        for k, v in temp:
            d[k].append(v)

        animal_info = get_animal_info(user)
        animal_data = []
        for the_animal in animal_info:
            for info in the_animal:
                animal_data.append(info)
        
        for k in d.keys():
            if k != '-1':
                coordinate_data.append(d[k][0])
                coordinate_data.append(animal_data)
                cluster_data.append(coordinate_data)   
                cluster_data.append(' ')
                coordinate_data = []
    
    return cluster_data


def get_coordinates(tracking_id, date,end_date):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select longitude,latitude from currentCoordinates where trackingID = %s and date >= %s and date < %s")
    cursor.execute(query, (tracking_id, date,end_date))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result


def get_associated_animals(user):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select trackingID from Animal where ownerID = BINARY %s")
    cursor.execute(query, (user,))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result

def get_animal_info(user):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select animalIdentifier, typeAnimal , breedAnimal , weightAnimal , genderAnimal , trackingID  from Animal where ownerID = BINARY %s")
    cursor.execute(query, (user,))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result

