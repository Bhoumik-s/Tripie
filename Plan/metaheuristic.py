import numpy as np
from random import randint
#route=np.array([[0,5,16,6,13,21],[0,12,9,3,4,21]])

# If route has more than 2 elements (i.e elemnts other than start and end point)
# Randomly select 2 elements and remove both the elements
# If both random number are same removes only 1 element
# Removed elements stored in rmvd
def MetaH1(route): 
	newRoute=[]
	rmvd=[]
	for i in range(route.shape[0]):
		if len(route[i])>2:
			p=randint(1,len(route[i])-2)
			q=randint(1,len(route[i])-2)
			if p==q:
				newRoute.append(np.delete(route[i],[p]))
			else:
				newRoute.append(np.delete(route[i],[p,q]))
		else:
			newRoute.append(route[i])
		rmvd.append(np.setdiff1d(route[i],newRoute[-1]))
	return (np.array(newRoute),rmvd)

# Randomly select 2 elements and remove all elements between them		
def MetaH2(route):
	newRoute=[]
	rmvd=[]
	for i in range(route.shape[0]):
		if len(route[i])>2:
			p=randint(1,len(route[i])-2)
			q=randint(1,len(route[i])-2)
			if p==q:
				newRoute.append(np.delete(route[i],[p]))
			else:
				c1=min(p,q)
				c2=max(p,q)
				newRoute.append(np.delete(route[i],range(c1,c2+1)))
		else:
			newRoute.append(route[i])
		rmvd.append(np.setdiff1d(route[i],newRoute[-1]))
	return (np.array(newRoute),rmvd)

# Randomly select 1 element and remove all elements till it from starting
def MetaH3(route):
	newRoute=[]
	rmvd=[]
	for i in range(route.shape[0]):
		if len(route[i])>2:
			p=randint(1,len(route[i])-2)
			newRoute.append(np.delete(route[i],range(1,p+1)))
		else:
			newRoute.append(route[i])
		rmvd.append(np.setdiff1d(route[i],newRoute[-1]))
	return (np.array(newRoute),rmvd)
