from data_class import Data
from constraints import status
from heuristic import heu1
from variables_class import Solution
from metaheuristic import metaN1,metaN2,metaN3
#from plot import plotPlan
import numpy as np
import time


def make_plan(city,days,start_time,end_time,budget):

	file=city+".xlsx"
	
	d=Data(file,days,start_time,end_time,budget)
	empty_route=np.array([[0,d.n+1]]*d.m)
	rmvd=[[]]*d.m

	sol=Solution(empty_route,d)
	new_sol= heu1(sol,rmvd,d)
	best_sol=new_sol
	best_p=status(new_sol,d)[1]
	iterations=0
	start_time = time.time()
	while (iterations<10 and (time.time() - start_time)<30):
		metaheu=1
		while(metaheu<=3):
			if metaheu==1:
				meta=metaN1(new_sol.R)
			if metaheu==2:
				meta=metaN2(new_sol.R)
			if metaheu==3:
				meta=metaN3(new_sol.R)
			sol=Solution(meta[0],d)
			rmvd=meta[1]
			new_sol=heu1(sol,rmvd,d)
			new_p=status(new_sol,d)[1]
			if new_p>best_p:
				best_p=new_p
				best_sol=new_sol
				metaheu=1
			else:
				metaheu=metaheu+1
		iterations=iterations+1
	no_of_locations=[]
	names=[]
	latitudes=[]
	longitudes=[]
	start=[]
	end=[]
	free=[]
	i=0
	for routes in (best_sol.R):
		no_of_locations.append(routes.shape[0])
		for destination in (routes):
			names.append(d.names[destination])
			latitudes.append(d.points[destination][0])
			longitudes.append(d.points[destination][1])
			start.append(best_sol.pi[destination][i])
			end.append(best_sol.pi[destination][i]+d.T[destination])
			free.append(best_sol.pi[destination][i]-best_sol.a[destination][i])
		i=i+1
	print time.time()
	return (no_of_locations,names,latitudes,longitudes,start,end,free)

#plotPlan(best_sol.R,d.points,d.m)



