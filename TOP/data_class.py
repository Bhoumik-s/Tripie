from read_data import read, find_segments
import numpy as np

class Data():
	def __init__(self,file,m,Tmax,Q):
		
		data=read(file)
		self.points=data[:,:2]
		self.t=find_segments(data[:,:2])
		self.happiness=data[:,2]
		self.cost=data[:,3]
		self.start_time=data[:,4]
		self.end_time=data[:,5]
		self.T=data[:,6]
		self.n=data.shape[0]-2
		self.m=m
		self.M=10000
		self.Tmax=Tmax
		self.Q=Q
