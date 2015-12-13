from data_class import DataClass
from constraints import Status
from heuristic import Heuristic
from variables_class import PlanVariables
from metaheuristic import MetaH1,MetaH2,MetaH3
import numpy as np
import time

MAXITERATIONS=2

# Algorithm Source: https://lirias.kuleuven.be/bitstream/123456789/276759/1/Garcia_etalv3_FINAL.pdf
# Initial feasible solution is created using HEU
# Elements are removed using MetaH#
# New Plan is made using heu

def MakePlan(Parameters):
	
	STARTTIME = time.time()
	Data=DataClass(Parameters)
	
	print time.time()-STARTTIME
	emptyRoute=np.empty((Data.DAYS,2), dtype=int)
	for i in range (Parameters.days):
		for j in range (2):
			emptyRoute[i,j]=Data.n+2*i+j

	rmvd=[[]]*Data.DAYS

	Plan=PlanVariables(emptyRoute,Data)
	heuristicResponse= Heuristic(Plan,rmvd,Data,Parameters.timeMultiplier)
	newPlan=heuristicResponse[0]
	bestPlan=newPlan
	bestObjective=heuristicResponse[1]
	
	iterations=0
	
	print time.time()-STARTTIME
	while (iterations<MAXITERATIONS and (time.time() - STARTTIME)<25):
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
			heuristicResponse=Heuristic(Plan,rmvd,Data,Parameters.timeMultiplier)
			newPlan=heuristicResponse[0]
			newObjective=heuristicResponse[1]
			
			if newObjective>bestObjective:
				bestObjective=newObjective
				bestPlan=newPlan
				metaheu=1
				iterations=0
			else:
				metaheu=metaheu+1
		iterations=iterations+1
		
	
	print time.time()-STARTTIME
	print bestObjective
	print bestPlan.route
	#return (no_of_locations,names,latitudes,longitudes,start,end,free)
	return [bestPlan,Data]

#plotPlan(bestPlan.route, Data.COORDINATES,Data.DAYS)



