from read_data import ReadData,ReadDurations
from Google_distance_API import duration_mat
import numpy as np

#DataClass fetches all constants for the trip
# time = minutes since 6AM in the morning

class DataClass():
	def __init__(self,CITY,DAYS,TMIN,TMAX,BUDGET,VISITED):
		
		dataFile=CITY+".xlsx"
		durationFile=CITY+"_duration.xls"
		file_data=ReadData(dataFile)
		cityDuration=ReadDurations(durationFile)
		cityData=file_data[0]
		
		DESTINATIONS=np.setdiff1d(range(len(cityData)),VISITED)
		self.n=len(DESTINATIONS)

		self.TRAVELTIME=[[0 for col in range(self.n)] for row in range(self.n)]
		data=[]
		self.NAMES=[]
		p=0

		for i in DESTINATIONS:
			data.append(cityData[i])
			self.NAMES.append(file_data[1][i]) #Names of places to visit
			q=0
			for j in DESTINATIONS:
				self.TRAVELTIME[p][q]=cityDuration[i][j]
				q=q+1
			p=p+1 
		
		self.TRAVELTIME=np.asarray(self.TRAVELTIME)
		data=np.asarray(data)
		self.COORDINATES=data[:,:2]
		#self.TRAVELTIME=duration_mat(self.COORDINATES[0:-1,0:2]) #Travel time between any two places
		#self.TRAVELTIME=ReadDurations('Mumbai_duration.xls')
		self.HAPPINESS=data[:,2] 
		self.COST=data[:,3]
		self.OPENTIME=data[:,4]
		#self.OPENTIME[0]=TMIN
		#self.OPENTIME[-1]=TMAX
		self.CLOSETIME=data[:,5]
		#self.CLOSETIME[0]=TMAX
		#self.CLOSETIME[-1]=TMAX
		self.SERVICETIME=data[:,6]
		self.n=data.shape[0]-2
		self.DAYS=DAYS
		self.M=10000
		self.TMAX=TMAX
		self.BUDGET=BUDGET
		self.TMIN=TMIN
