import numpy as np
#R=np.array([[0,5,16,6,13,21],[0,12,9,3,4,21]]).

class Solution:
    
    def reset(self,d):
        self.x=np.zeros((d.n+2,d.n+2,d.m))
        self.y=np.zeros((d.n+2,d.m))
        self.pi=np.zeros((d.n+2,d.m))
        self.a=np.zeros((d.n+2,d.m))
        self.a[0,:]=d.Tmin
        self.pi[0,:]=d.Tmin
        self.not_visited=np.array(range(1,d.n+1))
    
    def update(self,R,d):
        self.R=R
        self.reset(d)
        for i in range(d.m):
            self.not_visited=np.setdiff1d(self.not_visited,R[i])
            for j in range (len(R[i])-1):
                self.x[R[i][j],R[i][j+1],i]=1
                self.y[R[i][j],i]=1
                self.a[R[i][j+1],i]=self.pi[R[i][j],i]+d.T[R[i][j]]+d.t[R[i][j],R[i][j+1]]
                self.pi[R[i][j+1],i]=max(self.a[R[i][j+1],i],d.start_time[R[i][j+1]])
            self.y[R[i][-1],i]=1
    
    def __init__(self,R,d):
        self.R=R
        if np.sum(R!=0):
           self.update(R,d)
        else:
            self.reset(d)

