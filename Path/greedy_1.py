import time
import numpy as np



# Uses greedy approach to solve TSP

def find_segment_length(route,distance):
    segments=np.zeros(route.shape[0]-1)
    for i in range(route.shape[0]-1):
        segments[i]=distance[route[i]][route[i+1]]
    return segments

def next_point(not_visited,dis,points):
#selects points which is nearest and has not been visited
    mini=9999 
    for i in range (points.shape[0]):
        if (not_visited[i]) & (dis[i]>0) & (dis[i]<mini):
            mini=dis[i]
            nxt=i
    return nxt

def greedy(points,distance_mat):
    route = np.empty(0,dtype=int)  
    not_visited=np.ones(points.shape[0],dtype=bool) # True is point is not visited
    not_visited[0]=0
    route=np.append(route,0)
    now=0
    for i in range(points.shape[0]-1):
        dis=distance_mat[now][:] 
        nxt=next_point(not_visited,dis,points)
        route=np.append(route,nxt)
        not_visited[nxt]=0
        now=nxt
    route=np.append(route,0)
    travel_distance=np.sum(find_segment_length(route,distance_mat))
    return (travel_distance,route)





    
