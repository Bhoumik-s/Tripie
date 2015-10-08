from read_data import read
from Google_distance_API import duration_mat
import numpy as np

class Data():
	def __init__(self,file,m,Tmin,Tmax,Q):
		
		file_data=read(file)
		data=file_data[0]
		self.names=file_data[1]
		self.points=data[:,:2]
		self.t=duration_mat(self.points[0:-1,0:2])
		self.happiness=data[:,2]
		self.cost=data[:,3]
		self.start_time=data[:,4]
		self.start_time[0]=Tmin
		self.start_time[-1]=Tmax
		self.end_time=data[:,5]
		self.end_time[0]=Tmax
		self.end_time[-1]=Tmax
		self.T=data[:,6]
		self.n=data.shape[0]-2
		self.m=m
		self.M=10000
		self.Tmax=Tmax
		self.Q=Q
		self.Tmin=Tmin
