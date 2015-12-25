import datetime
import numpy as np

class ParameterClass():
	def __init__(self,request):	
	
		self.city = request.GET['City']
		self.deviceId = request.GET['deviceId']
		self.budget = 1500

		self.startTime = int(request.GET['StartTime'])
		self.endTime = int(request.GET['EndTime'])
		self.startDate = datetime.datetime.strptime(request.GET['StartDate'], '%d%m%Y')
		self.endDate = datetime.datetime.strptime(request.GET['EndDate'], '%d%m%Y')
		self.days = abs((self.endDate - self.startDate).days) + 1

		self.visited = np.array((request.GET['Visited']).split(","),dtype=int)
		self.interest = np.array((request.GET['Interest']).split(","),dtype=int)
		

		self.startLocation = np.array((request.GET['StartLocation']).split(","),dtype=float)
		self.stayLocation = np.array((request.GET['StayLocation']).split(","),dtype=float)
		
		firstCondition = [
						[self.startLocation[0],self.startLocation[1],
						self.stayLocation[0],self.stayLocation[1],
						self.startTime, 1080 + self.interest[3] * 90]
						]

		midCondition = [
						self.startLocation[0],self.startLocation[1],
						self.stayLocation[0],self.stayLocation[1],
						240 + self.interest[3] * 60, 1080 + self.interest[3] * 90
						]

		for i in range (self.days-1):
			firstCondition.append(midCondition)

		self.boundryConditions = np.asarray(firstCondition)	
		self.boundryConditions[-1,5] = self.endTime
		self.boundryConditions[-1,4] = min(self.endTime,self.boundryConditions[-1,4])

		self.timeMultiplier = min(6, 0.5 + sum([5,2.5,2,1.5,2] * self.interest[:]) )
		

		#print self.days
		#print self.boundryConditions
