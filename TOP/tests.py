from data_class import DataClass
import numpy as np
Visited=[]

BOUNDRYCONDITIONS=np.asarray([[18.944,72.823,18.944,72.823,300,720],[18.944,72.823,18.944,72.823,300,720],[18.944,72.823,18.944,72.823,300,720]])
Data=DataClass('Mumbai',3,1500,Visited,BOUNDRYCONDITIONS)

print Data.TRAVELTIME[0:5]
# Create your tests here.
