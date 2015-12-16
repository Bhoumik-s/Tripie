from collections import OrderedDict
import json
import os
import xlrd
import time
import getpass

def MakeJson(bestPlan,Data,Parameters,request):
	no_of_locations=[]
	names=[]
	locationId=[]
	latitudes=[]
	longitudes=[]
	start=[]
	end=[]
	free=[]
	i=0

	for routes in (bestPlan.route):
		no_of_locations.append(routes.shape[0])
		for destination in (routes):
			locationId.append(Data.ID[destination])
			latitudes.append(Data.COORDINATES[destination][0])
			longitudes.append(Data.COORDINATES[destination][1])
			start.append(bestPlan.pi[destination][i])
			end.append(bestPlan.pi[destination][i]+Data.SERVICETIME[destination])
			free.append(bestPlan.pi[destination][i]-bestPlan.a[destination][i])
		i=i+1

	response_data=OrderedDict()
	response_data["no_of_days"]=len(no_of_locations)
	response_data["no_of_locations"]=no_of_locations

	userInput = OrderedDict()
	userInput["City"] = request.GET['City']
	userInput["deviceId"] = request.GET['deviceId']
	userInput["StartTime"] = request.GET['StartTime']
	userInput["EndTime"] = request.GET['EndTime']
	userInput["StartDate"]=request.GET['StartDate']
	userInput["EndDate"]=request.GET['EndDate']
	userInput["Visited"]=request.GET['Visited']
	userInput['Interest']=request.GET['Interest']
	userInput['StayLocation']=request.GET['StayLocation']

	response_data["UserInput"]=userInput
	
	count=0

	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, "Mumbai.xlsx")
	book = xlrd.open_workbook(file_path)
	worksheet = book.sheet_by_index(0)

	plan_obj={}
	days=[]

	for i in range (len(no_of_locations)):
		location_list=[]
		location_obj={}
		for j in range (no_of_locations[i]):
			elements=OrderedDict()
			elements["locationId"]=locationId[count]
			elements["latitude"]=str(latitudes[count])
			elements["longitude"]=str(longitudes[count])
			elements["Start_time"]=str(start[count])
			elements["End_time"]=str(end[count])
			elements["Free_time"]=str(free[count])
			if (j==0):
				elements["Name"]= "Home/Start"
				elements["Description"]= " "
				elements["Timings"]= ""
				elements["Comment"] = ""
			elif (j==no_of_locations[i]-1):
				elements["Name"]= "Home"
				elements["Description"]= " "
				elements["Timings"]= ""
				elements["Comment"] = ""
			else:
				elements["Name"]= worksheet.cell(locationId[count]+1,13).value
				elements["Description"]= worksheet.cell(locationId[count]+1,16).value
				elements["Timings"]= worksheet.cell(locationId[count]+1,14).value
				elements["Comment"] = worksheet.cell(locationId[count]+1,15).value

			count=count+1
			location_list.append(elements)
		location_obj["location"]=location_list
		days.append(location_obj)
	plan_obj["Day"]=days
	response_data["Plan"]=plan_obj

	user = getpass.getuser()
	DIR = '/home/'+user+'/TripieServer/Plan/itineraries/'+Parameters.deviceId
	if not os.path.exists(DIR):
		os.makedirs(DIR)

	#fileName= len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
	fileName = time.strftime("%H:%M_%d:%m")
	file_path = os.path.join(DIR, fileName)
	

	with open(file_path, 'w') as outfile:
		outfile.write(json.dumps(response_data,outfile, indent=4, separators=(',', ': ')))
	
	return json.dumps(response_data, indent=4, separators=(',', ': '))