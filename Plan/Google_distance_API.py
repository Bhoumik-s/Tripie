import json
import requests
import numpy as np
from collections import OrderedDict

keys = ['AIzaSyAkyOPwCARgHCb5b7LK8XbWprn06HCXAzg',
		'AIzaSyD78YNBKealbLE70kG39MPvhYeS2Jv-1Eo',
		'AIzaSyDNKOkptxcE7y_kxb4SDJKEHMin9RjeDjo',	
		'AIzaSyDxqD0Xsl10vU8cOLD9dPQ8jk0vGaLDX7A',	
		'AIzaSyA73nFAZ1v7kUbDzuWEQ4VgdqJJCU60X4I',
		'AIzaSyCk2DyMbghRyaGPlqyaYxyan72tn_4hDec',
		'AIzaSyBN43Q0fg989SwKqLLBfx3pyuj5_cTnW5A',
		'AIzaSyDtbnG0hUFeRoWX-GtUOSeNImNBn1JvTsw',
		'AIzaSyB4AqTl8IvqNRMD_U9ALLUUiw6KcIP5a_0',
		'AIzaSyB5juy1Uvotz6dSx2bQ6s2Ii4SgGxq3EH0']

def GetResponse(origins,destinations,keyId):
		url='https://maps.googleapis.com/maps/api/distancematrix/json'	
		params = OrderedDict(
			origins= origins,
			destinations=destinations,
			key=keys[keyId]
			)


		resp = requests.get(url=url, params=params)
		data = json.loads(resp.text)

		if data['status']=='OK':
			return (keyId,data)
		else:
			keyId=(keyId+1%9)
			return GetResponse(origins,destinations,keyId)

def FindDurations(originCo,destinationCo):
	keyId=7
	origins=str(originCo[0])+','+str(originCo[1])
	
	destinations=str(destinationCo[0][0])+','+str(destinationCo[0][1])
	for i in range (1,destinationCo.shape[0]):
	    destinations= destinations+'|'+str(destinationCo[i][0])+','+str(destinationCo[i][1])
	
	
	resp=GetResponse(origins,destinations,keyId)
	keyId=resp[0]
	data=resp[1]
	
	durations=np.zeros(destinationCo.shape[0],dtype=int)

	for k in range(destinationCo.shape[0]):
			durations[k]=data['rows'][0]['elements'][k]['duration']['value']/60
	

	return durations
	