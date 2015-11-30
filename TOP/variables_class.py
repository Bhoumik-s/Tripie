import numpy as np

# it takes route as an input
# e.g route=[[0,1,5,7,9,0],[0,6,4,11,0]]

# This class stores various properties of a solution
# These properties decides feasibiity and objective of solution

# x(i,j,k) = 1 if visit to i is followed by j on day k ie i first then j
# y(i,k) = 1 if i is visited on day k
# pi(i,k) = begining time of destination i on day k
#         = 0 if i is not visited on day k
# (time = minutes since 5AM in the morning)
# a(i,k) = arrival time at i on day k
#        = 0 if i is not visited on day k
# notVisited = list of places not visited during whole trip

class PlanVariables:
	
	def reset(self,Data):
		self.x=np.zeros((Data.n+2*Data.DAYS,Data.n+2*Data.DAYS,Data.DAYS))
		self.y=np.zeros((Data.n+2*Data.DAYS,Data.DAYS))
		self.pi=np.zeros((Data.n+2*Data.DAYS,Data.DAYS))
		self.a=np.zeros((Data.n+2*Data.DAYS,Data.DAYS))
		
		self.notVisited=np.array(range(Data.n))

	# notVisited is set diff of All places and places in route
	# a = pi(previous) + ServiceTime(previous) + TravelTime
	# pi = max (a, StartTime)
	
	def update(self,route,Data):
		self.route=route
		self.reset(Data)
		
		for i in range(Data.DAYS):
			self.a[route[i][0],i]=Data.TMIN[i]
			self.pi[route[i][0],i]=Data.TMIN[i]
			self.notVisited=np.setdiff1d(self.notVisited,route[i])
			for j in range (len(route[i])-1):
				self.x[route[i][j],route[i][j+1],i]=1
				self.y[route[i][j],i]=1
				self.a[route[i][j+1],i]=(self.pi[route[i][j],i]+Data.SERVICETIME[route[i][j]]
									+Data.TRAVELTIME[route[i][j],route[i][j+1]])
				self.pi[route[i][j+1],i]=max(self.a[route[i][j+1],i],Data.OPENTIME[route[i][j+1]])
			self.y[route[i][-1],i]=1
	
	def __init__(self,route,Data):
		self.route=route
		self.update(route,Data)

