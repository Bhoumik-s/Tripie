import numpy as np

# Checks all constranints for a soluions
# Return = [True , ObjectiveValue]
# Or     = [False , Failed Constraint]
# Redundant 2,6

def Status(Plan,Data):
	x=Plan.x
	y=Plan.y
	pi=Plan.pi
	
	def Objective():
		happiness=0
		for i in range(Data.DAYS):
			for j in range (1,Data.n+1):
				happiness=happiness+Data.HAPPINESS[j]*y[j,i]
		return happiness

	def BudgetConstraint():
		sum1=0
		for k in range(Data.DAYS):
			for i in range(1,Data.n+1):
				sum1=sum1+Data.COST[i]*y[i,k]
		boolean=(sum1<=Data.BUDGET)
		if boolean:
			return [boolean,Objective()]
		else:
			return [False,2]


	#Service start time at each point <= closingTime
	def TimeConstraint():
		boolean=True
		for k in range(Data.DAYS):
			for i in range (Data.n+2):
				boolean=(boolean and (pi[i,k]<=Data.CLOSETIME[i]))
		if boolean:
			return BudgetConstraint()
		else:
			return [False,1]

	return (TimeConstraint())
 
	# for each day time to return should be less than T_max
	# Return time = arrival time(a) at final point
	'''
	def TimeConstraint():
		boolean=True
		for k in range(Data.DAYS):
			boolean= (boolean and (Plan.a[Data.n+1,k]<=Data.TMAX))
		if boolean:
			return [boolean,Objective()]
		else:
			return [False,7]
			'''
	# if visit to i is followed by visit to j arrivalTime(j)<serviceStartSime(j)
	"""
	def ContinuityConstraint():B
		for i in range(Data.n+2):
			for j in range(Data.n+2):
				for k in range (Data.DAYS):
					boolean=(boolean and (a[j,k]-pi[j,k]<=Data.M*(1-x[i,j,k])))
		if boolean:
			return TimeConstraint()
		else:
			return [False,6]
			"""
	## if i is visited on day k there is exactly one preceding and following point		
	'''
	def OneVertexConstraint():
		boolean=True
		for i in range(1,Data.n+1):
			for k in range(Data.DAYS):
				sum1=np.sum(x[0:Data.n+1,i,k])
				sum2=np.sum(x[i,1:Data.n+2,k])
				boolean=(boolean and ((sum1==sum2) and (sum1==y[i,k])))
		if boolean:
			return TimeConstraint()
		else:
			return [False,5]
			'''
	#Each point is visited only once during all days 
	'''
	def OnceConstraint():
		boolean=True
		for h in range(1,Data.n+1):
			boolean=(boolean and (np.sum(y[h,:])<=1))
		if boolean:
			return BudgetConstraint()
		else:
			return [False,3]
			'''

	'''	
	def DaysConstraint():
		sum1=np.sum(x[0,1:Data.n+2,:])
		sum2=np.sum(x[0:Data.n+1,Data.n+1,:])
		if (((sum1==sum2) and (sum1==Data.DAYS))):
			return OnceConstraint()
		else:
			return [False,2]
			'''