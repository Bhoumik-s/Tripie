from django.shortcuts import render
import json
from xlrd import open_workbook
from xlutils.copy import copy
from django.http import HttpResponse
import os
import time
from django.utils import timezone
from .models import User
from django.utils import timezone

def CheckId(deviceId,mob):
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'UserData.xls')
	oldBook = open_workbook(file_path)
	worksheet = oldBook.sheet_by_index(0)
	n=worksheet.nrows
	for i in range (n-1):
		if (deviceId==worksheet.cell(i+1,1).value):
			return True
	signUpDate = time.strftime("%d/%m/%y")
	signUpTime = time.strftime("%H:%M:%S")
	book = copy(oldBook)
	sheet = book.get_sheet(0)
	sheet.write(n,0,mob)
	sheet.write(n,1,deviceId)
	sheet.write(n,2,signUpTime)
	sheet.write(n,3,signUpDate)
	book.save(file_path)
	
	if not User.objects.filter(deviceId=deviceId).exists():
		user = User(deviceId=deviceId,mobile=mob,accessToken=deviceId)
		user.save()

	return False
	
# Create your views here.
def home(request):

	mob=request.GET['mob']
	deviceId=request.GET['deviceId']
	CheckId(deviceId,mob)
	response_data={}
	response_data["key"]=deviceId
	return HttpResponse(json.dumps(response_data))

'''
def AddNewDevice(deviceId,mob):
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'UserData.xls')
 	oldBook = open_workbook(file_path,formatting_info=True)
 	oldSheet = oldBook.sheet_by_index(0) 
 	n = oldSheet.nrows
	book = copy(oldBook)
	sheet = book.get_sheet(0)
	sheet.write(n,0,mob)
	sheet.write(n,1,deviceId)
	book.save(file_path)
	'''