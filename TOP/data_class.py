from read_data import read
from Google_distance_API import duration_mat
import numpy as np

#DataClass fetches all constants for the trip

class DataClass():
	def __init__(self,file,DAYS,TMIN,TMAX,BUDGET):
		
		file_data=read(file)
		data=file_data[0]
		self.NAMES=file_data[1]
		self.COORDINATES=data[:,:2]
		self.TRAVELTIME=duration_mat(self.COORDINATES[0:-1,0:2])
		self.HAPPINESS=data[:,2]
		self.COST=data[:,3]
		self.OPENTIME=data[:,4]
		self.OPENTIME[0]=TMIN
		self.OPENTIME[-1]=TMAX
		self.CLOSETIME=data[:,5]
		self.CLOSETIME[0]=TMAX
		self.CLOSETIME[-1]=TMAX
		self.SERVICETIME=data[:,6]
		self.n=data.shape[0]-2
		self.DAYS=DAYS
		self.M=10000
		self.TMAX=TMAX
		self.BUDGET=BUDGET
		self.TMIN=TMIN
