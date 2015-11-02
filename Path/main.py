import numpy as np
from opt_2 import opt2
from greedy_1 import greedy

def find_distance(points):
    distance=np.zeros((points.shape[0],points.shape[0]))
    for i in range(points.shape[0]):
        for j in range (i+1, points.shape[0]):
            distance[i][j]=pow(pow(points[i][0]-points[j][0],2)+pow(points[i][1]-points[j][1],2),0.5)
            distance[j][i]=distance[i][j]
    return distance

def OptiPath(points):
    distance_mat=find_distance(points)
    greedyResult=greedy(points,distance_mat)
    opt2Result=opt2(points,distance_mat)
    return(greedyResult,opt2Result)


   
   
