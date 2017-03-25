from flask import Flask,json
from connector import create_connection
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from collections import defaultdict


def cluster(animalIdentifier, trackingNumber,date):
    #http://geoffboeing.com/2014/08/clustering-to-reduce-spatial-data-set-size/
    if animalIdentifier =='' or trackingNumber =='' or date == '':
        overallResult = json.dumps({"status": "Empty Fields"})
        return overallResult
        
    data = get_coordinates(trackingNumber,date)
    if len(data)<=1:
        overallResult = json.dumps({"status": "No Data"})
        return overallResult
        
    kms_per_radian = 6371.0088
    eps = .005/kms_per_radian
    coordinates =[]
    temp_data =[]
    for elements in data:
        for items in elements:
            temp_data.append(float(items))
        coordinates.append(temp_data)
        temp_data=[]

    coords = np.matrix(coordinates)
    #min_samples =1 means every point get assigned to a cluster or becomes a cluster itself
    #ball_tree algorithm hyper spheres multidimensional each point belongs to one sphere only
    #ball_tree partition data into nested spheres, more costly than kd tree more efficient multidimensional
    db = DBSCAN(eps, min_samples=3, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    #kmeans requires you to specify the number of clusters in advance which dbscan doesnt it uses eps and min_samples
    cluster_labels = db.labels_
    clusters = set(cluster_labels)
    num_clusters = len(set(cluster_labels))
    #core samples:  A point is a core point if it has more than a specified number of points (MinPts) within Eps—These are points that are at the interior of a cluster.
    temp =[]
    elements = {}
    for i,element in enumerate(cluster_labels):
        coordinate = data[i]
        temp.append((str(element),[coordinate[0],coordinate[1]]))

    
    d = defaultdict(list)
    for k,v in temp:
        d[k].append(v)

    coordinates =[]
    for k in d.keys():
        if k != '-1':
            coordinates.append(d[k][0])

    return coordinates


def get_coordinates(trackingID,date):
    cnx2 = create_connection()
    cursor = cnx2.cursor()
    query = ("Select longitude,latitude from currentCoordinates where trackingID = %s and date >= %s")
    cursor.execute(query,(trackingID,date))
    result = cursor.fetchall()
    cursor.close()
    cnx2.close()
    return result



