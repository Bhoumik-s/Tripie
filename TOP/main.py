from data_class import DataClass
from constraints import Status
from heuristic import Heuristic
from variables_class import PlanVariables
from metaheuristic import MetaH1,MetaH2,MetaH3
import numpy as np
import time

MAXITERATIONS=10

# Algorithm Source: https://lirias.kuleuven.be/bitstream/123456789/276759/1/Garcia_etalv3_FINAL.pdf
# Initial feasible solution is created using HEU
# Elements are removed using MetaH#
# New Plan is made using heu

def make_plan(CITY,DAYS,TMIN,TMAX,BUDGET):

	
	
	Data=DataClass(CITY,DAYS,TMIN,TMAX,BUDGET,[])
	emptyRoute=np.array([[0,Data.n+1]]*Data.DAYS)
	rmvd=[[]]*Data.DAYS

	Plan=PlanVariables(emptyRoute,Data)
	newPlan= Heuristic(Plan,rmvd,Data)
	bestPlan=newPlan
	bestObjective=Status(newPlan,Data)[1]
	
	iterations=0
	STARTTIME = time.time()

	while (iterations<MAXITERATIONS and (time.time() - STARTTIME)<30):
		metaheu=1
		
		while(metaheu<=3):
			if metaheu==1:
				meta=MetaH1(newPlan.route)
			if metaheu==2:
				meta=MetaH2(newPlan.route)
			if metaheu==3:
				meta=MetaH3(newPlan.route)
			
			Plan=PlanVariables(meta[0],Data)
			rmvd=meta[1]
			newPlan=Heuristic(Plan,rmvd,Data)
			newObjective=Status(newPlan,Data)[1]
			
			if newObjective>bestObjective:
				bestObjective=newObjective
				bestPlan=newPlan
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
	
	for routes in (bestPlan.route):
		no_of_locations.append(routes.shape[0])
		for destination in (routes):
			names.append(Data.NAMES[destination])
			latitudes.append(Data.COORDINATES[destination][0])
			longitudes.append(Data.COORDINATES[destination][1])
			start.append(bestPlan.pi[destination][i])
			end.append(bestPlan.pi[destination][i]+Data.SERVICETIME[destination])
			free.append(bestPlan.pi[destination][i]-bestPlan.a[destination][i])
		i=i+1
	
	print time.time()-STARTTIME
	
	return (no_of_locations,names,latitudes,longitudes,start,end,free)

#plotPlan(bestPlan.route,Data.COORDINATES,Data.DAYS)



