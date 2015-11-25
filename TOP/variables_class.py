import numpy as np
#R=np.array([[0,5,16,6,13,21],[0,12,9,3,4,21]]).

class Solution:
    
    def reset(self,data):
        self.x=np.zeros((data.n+2,data.n+2,data.days))
        self.y=np.zeros((data.n+2,data.days))
        self.pi=np.zeros((data.n+2,data.days))
        self.a=np.zeros((data.n+2,data.days))
        self.a[0,:]=data.Tmin
        self.pi[0,:]=data.Tmin
        self.not_visited=np.array(range(1,data.n+1))
    
    def update(self,R,data):
        self.R=R
        self.reset(data)
        for i in range(data.days):
            self.not_visited=np.setdiff1d(self.not_visited,R[i])
            for j in range (len(R[i])-1):
                self.x[R[i][j],R[i][j+1],i]=1
                self.y[R[i][j],i]=1
                self.a[R[i][j+1],i]=self.pi[R[i][j],i]+data.serviceTime[R[i][j]]+data.travelTime[R[i][j],R[i][j+1]]
                self.pi[R[i][j+1],i]=max(self.a[R[i][j+1],i],data.start_time[R[i][j+1]])
            self.y[R[i][-1],i]=1
    
    def __init__(self,R,data):
        self.R=R
        if np.sum(R!=0):
           self.update(R,data)
        else:
            self.reset(data)

