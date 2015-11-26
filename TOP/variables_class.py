import numpy as np

# it takes route as an input
# e.g R=[[0,1,5,7,9,0],[0,6,4,11,0]]

# This class stores various properties of a solution
# These properties decides feasibiity and objective of solution

# x(i,j,k) = 1 if visit to i is followed by j on day k ie i first then j
# y(i,k) = 1 if i is visited on day k
# pi(i,k) = begining time of destination i on day k
#         = 0 if i is not visited on day k
# (time = minutes since 5AM in the morning)
# a(i,k) = arrival time at i on day k
#        = 0 if i is not visited on day k
# not_visited = list of places not visited during whole trip

class Solution:
	
	def reset(self,data):
		self.x=np.zeros((data.n+2,data.n+2,data.DAYS))
		self.y=np.zeros((data.n+2,data.DAYS))
		self.pi=np.zeros((data.n+2,data.DAYS))
		self.a=np.zeros((data.n+2,data.DAYS))
		self.a[0,:]=data.TMIN
		self.pi[0,:]=data.TMIN
		self.not_visited=np.array(range(1,data.n+1))

	# not_visited is set diff of All places and places in R
	# a = pi(previous) + ServiceTime(previous) + TravelTime
	# pi = max (a, StartTime)
	
	def update(self,R,data):
		self.R=R
		self.reset(data)
		for i in range(data.DAYS):
			self.not_visited=np.setdiff1d(self.not_visited,R[i])
			for j in range (len(R[i])-1):
				self.x[R[i][j],R[i][j+1],i]=1
				self.y[R[i][j],i]=1
				self.a[R[i][j+1],i]=(self.pi[R[i][j],i]+data.SERVICETIME[R[i][j]]
									+data.TRAVELTIME[R[i][j],R[i][j+1]])
				self.pi[R[i][j+1],i]=max(self.a[R[i][j+1],i],data.OPENTIME[R[i][j+1]])
			self.y[R[i][-1],i]=1
	
	def __init__(self,R,data):
		self.R=R
		self.update(R,data)

