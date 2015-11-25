from read_data import read
from Google_distance_API import duration_mat
import numpy as np

class DataClass():
	def __init__(self,file,days,Tmin,Tmax,budget):
		
		file_data=read(file)
		data=file_data[0]
		self.names=file_data[1]
		self.coordinate=data[:,:2]
		self.travelTime=duration_mat(self.coordinate[0:-1,0:2])
		self.happiness=data[:,2]
		self.cost=data[:,3]
		self.openTime=data[:,4]
		self.openTime[0]=Tmin
		self.openTime[-1]=Tmax
		self.closeTime=data[:,5]
		self.closeTime[0]=Tmax
		self.closeTime[-1]=Tmax
		self.serviceTime=data[:,6]
		self.n=data.shape[0]-2
		self.days=days
		self.M=10000
		self.Tmax=Tmax
		self.budget=budget
		self.Tmin=Tmin
