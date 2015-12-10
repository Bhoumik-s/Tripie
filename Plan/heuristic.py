import numpy as np
from variables_class import PlanVariables
from constraints import Status

# Insert all possible candidates at all possible positions
# Candidates = NotVisited - Removed during last metaheuristic
# Adding each candidate has some cost
# cost = page 7 of algo source
# candidate with minimum cost at a place is added
# if it gives feasible solution newPlan is updated

# (a 1 , a 2 ) = {(0.9, 0.1), (0.7, 0.3), (0.5, 0.5)}.
# b = {0.9, 0.7, 0.5, 0.3, 0.1}
# g = {2, 3, 4}
para=[0.9,0.1,0.9,2]

def InsertElement(route,element,position):
	newRoute = []
	tempRoute = np.delete(route,position[0],0)
	tempPlan = np.insert(route[position[0]],position[1],element)
	j = 0
	for day in range(route.shape[0]):
		if day==position[0]:
		   newRoute.append(tempPlan)
		else:
			newRoute.append(tempRoute[j])
			j = j + 1
	return np.array(newRoute)


def CalculateCost(Plan,tempPlan,day,j,enteringElement,Data):

	N1 = float(para[0]*(Data.TRAVELTIME[Plan.route[day][j-1],enteringElement]
				+Data.TRAVELTIME[enteringElement,Plan.route[day][j]]
				-Data.TRAVELTIME[Plan.route[day][j-1],Plan.route[day][j]] 
				+ para[2]*Data.SERVICETIME[enteringElement]))

	N2 = float(para[1]*(tempPlan.pi[tempPlan.route[day][j+1],day]
		-tempPlan.pi[Plan.route[day][j],day]))

	N3 = float(Data.HAPPINESS[enteringElement]**para[3])

	return float((N1+N2)/N3)


def Heuristic(Plan,rmvd,Data):
	newPlan=Plan
	
	for day in range (newPlan.route.shape[0]):
		j=1
		
		while j<len(newPlan.route[day]):
			candidates=np.setdiff1d(newPlan.notVisited,rmvd[day])
			flag=0
			update=0
			minCost=999

			for enteringElement in (candidates):
				tempRoute=InsertElement(newPlan.route,enteringElement,[day,j])
				tempPlan=PlanVariables(tempRoute,Data)
				cost=CalculateCost(newPlan,tempPlan,day,j,enteringElement,Data)
				status=Status(tempPlan,Data)
				if (cost<minCost and status[0]):
					minCost=cost
					flag=1
					update=tempPlan
				#else:
				#	print Status(tempPlan,Data)

			if flag==1:
				j=0
				newPlan=update

			j=j+1
				
	return (newPlan,status[1])
				
					
					
				
				
			
			
			
