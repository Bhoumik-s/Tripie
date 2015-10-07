import numpy as np
from variables_class import Solution
from read_data import read, find_segments
from constraints import status


def insert_element(R,element,position):
    new_R=[]
    R_temp=np.delete(R,position[0],0)
    temp = np.insert(R[position[0]],position[1],element)
    j=0
    for i in range(R.shape[0]):
        if i==position[0]:
           new_R.append(temp)
        else:
            new_R.append(R_temp[j])
            j=j+1
    return np.array(new_R)

def cost1(sol,temp,para,i,j,v,d):
    N1=float(para[0]*(d.t[sol.R[i][j-1],v]+d.t[v,sol.R[i][j]]-d.t[sol.R[i][j-1],sol.R[i][j]] + para[2]*d.T[v]))
    #print temp.pi[temp.R[i][j+1],i]
    N2=float(para[1]*(temp.pi[temp.R[i][j+1],i]-temp.pi[sol.R[i][j],i]))
    D=float(d.happiness[v]**para[3])
    return float((N1+N2)/D)

def heu1(sol,rmvd,d):
    sol_temp=sol
    not_visited=sol_temp.not_visited
    not_visited=np.union1d(not_visited,[item for sublist in rmvd for item in sublist])
    
    for i in range (sol_temp.R.shape[0]):
        to_be_visited=np.setdiff1d(not_visited,rmvd[i])
        j=1
        while j<len(sol_temp.R[i]):
            flag=0
            update=0
            min_cost=999
            for v in (to_be_visited):
                R_temp=insert_element(sol_temp.R,v,[i,j])
                temp=Solution(R_temp,d)
                cost=cost1(sol_temp,temp,[0.9,0.1,0.9,2],i,j,v,d)
                if (cost<min_cost and status(temp,d)[0]):
                    min_cost=cost
                    flag=1
                    update=temp
            if flag==1:
                j=0
                sol_temp=update
            j=j+1
    
    for i in range (sol_temp.R.shape[0]):
        while j<len(sol_temp.R[i]):
            flag=0
            update=0
            min_cost=999
            for v in (rmvd[i]):
                R_temp=insert_element(sol_temp.R,v,[i,j])
                temp=Solution(R_temp,d)
                cost=cost1(sol_temp,temp,[0.9,0.1,0.9,2],i,j,v,d)
                if (cost<min_cost and status(temp,d)[0]):
                    min_cost=cost
                    flag=1
                    update=temp
            if flag==1:
                j=0
                sol_temp=update
            j=j+1

                
    return sol_temp
                
                    
                    
                
                
            
            
            
