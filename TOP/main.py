from data_class import DataClass
from constraints import status
from heuristic import heu1
from variables_class import Solution
from metaheuristic import metaN1,metaN2,metaN3
import numpy as np
import time

#Algorithm Source: https://lirias.kuleuven.be/bitstream/123456789/276759/1/Garcia_etalv3_FINAL.pdf

def make_plan(city,DAYS,tMin,tMax,BUDGET):

	file=city+".xlsx"
	
	data=DataClass(file,DAYS,tMin,tMax,BUDGET)
	empty_route=np.array([[0,data.n+1]]*data.DAYS)
	rmvd=[[]]*data.DAYS

	sol=Solution(empty_route,data)
	new_sol= heu1(sol,rmvd,data)
	best_sol=new_sol
	best_p=status(new_sol,data)[1]
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
			sol=Solution(meta[0],data)
			rmvd=meta[1]
			new_sol=heu1(sol,rmvd,data)
			new_p=status(new_sol,data)[1]
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
			names.append(data.NAMES[destination])
			latitudes.append(data.COORDINATES[destination][0])
			longitudes.append(data.COORDINATES[destination][1])
			start.append(best_sol.pi[destination][i])
			end.append(best_sol.pi[destination][i]+data.SERVICETIME[destination])
			free.append(best_sol.pi[destination][i]-best_sol.a[destination][i])
		i=i+1
	print time.time()
	return (no_of_locations,names,latitudes,longitudes,start,end,free)

#plotPlan(best_sol.R,data.COORDINATES,data.DAYS)



