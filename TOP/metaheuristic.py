import numpy as np
from random import randint
R=np.array([[0,5,16,6,13,21],[0,12,9,3,4,21]])

def metaN1(R):
    temp=[]
    rmvd=[]
    for i in range(R.shape[0]):
        p=randint(1,len(R[i])-2)
        q=p
        while q==p:
            q=randint(1,len(R[i])-2)
        temp.append(np.delete(R[i],[p,q]))
        rmvd.append(np.setdiff1d(R[i],temp[-1]))
    return (np.array(temp),rmvd)
        
def metaN2(R):
    temp=[]
    rmvd=[]
    for i in range(R.shape[0]):
        p=randint(1,len(R[i])-2)
        q=p
        while q==p:
            q=randint(1,len(R[i])-2)
        c1=min(p,q)
        c2=max(p,q)
        temp.append(np.delete(R[i],range(c1,c2+1)))
        rmvd.append(np.setdiff1d(R[i],temp[-1]))
    return (np.array(temp),rmvd)

def metaN3(R):
    temp=[]
    rmvd=[]
    for i in range(R.shape[0]):
        p=randint(1,len(R[i])-2)
        temp.append(np.delete(R[i],range(1,p+1)))
        rmvd.append(np.setdiff1d(R[i],temp[-1]))
    return (np.array(temp),rmvd)
