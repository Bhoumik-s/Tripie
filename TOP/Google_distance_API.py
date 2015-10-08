import json
import requests
import numpy as np
from collections import OrderedDict

def duration_mat(coordinates):
	url='https://maps.googleapis.com/maps/api/distancematrix/json'
	n=coordinates.shape[0]
	
	places=str(coordinates[0][0])+','+str(coordinates[0][1])
	for i in range (1,n):
	    places= places+'|'+str(coordinates[i][0])+','+str(coordinates[i][1])
	
	#params = dict(
    #	origins='Hostel 6, Indian Institute of Technology Bombay, Main Gate Path, Students Residential Zone, IIT Area, Powai, Mumbai, Maharashtra 400076, India|18.922367,72.833698',
    #	destinations='Hostel 6, Indian Institute of Technology Bombay, Main Gate Path, Students Residential Zone, IIT Area, Powai, Mumbai, Maharashtra 400076, India|18.922367,72.833698',
    #	key='AIzaSyAkyOPwCARgHCb5b7LK8XbWprn06HCXAzg'
	#)
	params = OrderedDict(
		origins= places,
	    destinations=places,
	    #key='AIzaSyAkyOPwCARgHCb5b7LK8XbWprn06HCXAzg'
	    key='AIzaSyD78YNBKealbLE70kG39MPvhYeS2Jv-1Eo'
	)
	#print params
	resp = requests.get(url=url, params=params)
	data = json.loads(resp.text)
	distances=np.zeros((n+1,n+1),dtype=int)
	durations=np.zeros((n+1,n+1),dtype=int)

	for i in range(n):
		for j in range(n):
			distances[i][j]=data['rows'][i]['elements'][j]['distance']['value']/1000
			durations[i][j]=data['rows'][i]['elements'][j]['duration']['value']/60
	durations[-1,:]=durations[0,:]
	durations[:,-1]=durations[:,0]
	return durations
	