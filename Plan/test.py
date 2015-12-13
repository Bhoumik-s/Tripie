from main import make_plan
import numpy as np
Visited=[]
#Visited=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
BOUNDRYCONDITIONS=np.asarray([[19.1352711,72.9048303,19.1352711,72.9048303,240,1180],[19.1352711,72.9048303,19.1352711,72.9048303,240,1180]])
x=make_plan('Mumbai',2,1500,Visited,BOUNDRYCONDITIONS)
print x