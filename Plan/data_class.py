from read_data import ReadData,ReadDurations
from Google_distance_API import FindDurations
import numpy as np

#DataClass fetches all constants for the trip
# time = minutes since 5AM in the morning

class DataClass():
	def __init__(self,Parameters):

		CITY = Parameters.city
		DAYS = Parameters.days
		BUDGET = Parameters.budget
		VISITED = Parameters.visited
		BOUNDRYCONDITIONS = Parameters.boundryConditions
		INTEREST = Parameters.interest
		
		dataFile=CITY+".xlsx"
		durationFile=CITY+"_duration.xls"
		file_data=ReadData(dataFile)
		cityDuration=ReadDurations(durationFile)
		cityData=file_data[0]
		
		DESTINATIONS=np.setdiff1d(range(len(cityData)),VISITED)
		self.n=len(DESTINATIONS)

		self.TRAVELTIME=np.zeros((self.n+2*DAYS,self.n+2*DAYS))
		data=[]
		self.NAMES=[]

		p=0
		for i in DESTINATIONS:
			data.append(cityData[i])
			self.NAMES.append(file_data[1][i]) #Names of places to visit
			q=0
			for j in DESTINATIONS:
				self.TRAVELTIME[p,q]=cityDuration[i][j]
				q=q+1
			p=p+1 

		data=np.asarray(data)
		self.ID = data[:,0]
		self.COORDINATES=data[:,1:3]
		self.HAPPINESS=data[:,3]+(data[:,4:9]*INTEREST).sum(axis=1)
		self.COST=data[:,9]
		self.OPENTIME=np.append(data[:,10],np.zeros((2*DAYS,1)))
		self.CLOSETIME=data[:,11]
		self.SERVICETIME=np.append(data[:,12],np.zeros((2*DAYS,1)))
		self.DAYS=DAYS
		self.TMAX=BOUNDRYCONDITIONS[:,5]
		self.BUDGET=BUDGET
		self.TMIN=BOUNDRYCONDITIONS[:,4]
		
		keyId=0
		GoogleResp=FindDurations([BOUNDRYCONDITIONS[0][0],BOUNDRYCONDITIONS[0][1]],self.COORDINATES,keyId)
		startDuration = GoogleResp[0]
		if ( (BOUNDRYCONDITIONS[0][0] == BOUNDRYCONDITIONS[0][2]) and (BOUNDRYCONDITIONS[0][1] == BOUNDRYCONDITIONS[0][3]) ):
			stayDuration = GoogleResp[0]
		else:
			keyId=GoogleResp[1]
			GoogleResp=FindDurations([BOUNDRYCONDITIONS[0][2],BOUNDRYCONDITIONS[0][3]],self.COORDINATES,keyId)
			stayDuration = GoogleResp[0]

		self.TRAVELTIME[self.n,0:self.n]=startDuration
		self.TRAVELTIME[0:self.n,self.n]=startDuration[:]
		self.TRAVELTIME[self.n+1,0:self.n]=stayDuration
		self.TRAVELTIME[0:self.n,self.n+1]=stayDuration[:]

		if (DAYS > 1) :
			for i in range (1,DAYS):
				for j in range(2):
					self.TRAVELTIME[self.n+2*i+j,0:self.n]=stayDuration
					self.TRAVELTIME[0:self.n,self.n+2*i+j]=stayDuration[:]

		for i in range (DAYS):
			self.NAMES.append("Home/Start")
			self.NAMES.append("Home")
			for j in range(2):		
				self.ID = np.append(self.ID,cityData.shape[0]+j)
				newCoordinates = [BOUNDRYCONDITIONS[i][2*j],BOUNDRYCONDITIONS[i][2*j+1]]
				self.COORDINATES = np.vstack([self.COORDINATES,newCoordinates])
