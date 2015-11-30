import json
import requests
import numpy as np
from collections import OrderedDict
from read_data import read
import xlwt

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
			#traffic_model= 'pessimistic'
			)
		#print params
		resp = requests.get(url=url, params=params)
		data = json.loads(resp.text)
		#print data['status']
		if data['status']=='OK':
			return (keyId,data)
		else:
			keyId=(keyId+1%9)
			return GetResponse(origins,destinations,keyId)


def GetDurationMat(city):
	keyId=0

	file=city+'.xlsx'
	coordinates=read(file)
	
	n=coordinates.shape[0]
	durations=np.zeros((n,n),dtype=int)
	
	for i in range (0,n):
		print i
		origins=str(coordinates[i][0])+','+str(coordinates[i][1])
		destinations=str(coordinates[0][0])+','+str(coordinates[0][1])
		
		for j in range (1,n):
			destinations=destinations+'|'+str(coordinates[j][0])+','+str(coordinates[j][1])
		
		resp=GetResponse(origins,destinations,keyId)
		keyId=resp[0]
		data=resp[1]		
		for k in range(n):
			durations[i,k]=data['rows'][0]['elements'][k]['duration']['value']/60

	book = xlwt.Workbook()
	bookName="Mumbai_duration.xls"
	sheetName="6.30 PM"
	sheet = book.add_sheet(sheetName)

	for i in range (n):
		for j in range (n):
			sheet.write(i,j,durations[i][j])
	book.save(bookName)