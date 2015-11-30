from main import make_plan
import numpy as np
Visited=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
BOUNDRYCONDITIONS=np.asarray([[18.944,72.823,18.944,72.823,300,720],[18.944,72.823,18.944,72.823,300,720],[18.944,72.823,18.944,72.823,300,720]])
x=make_plan('Mumbai',3,1500,Visited,BOUNDRYCONDITIONS)
print x