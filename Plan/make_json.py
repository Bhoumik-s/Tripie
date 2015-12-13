from collections import OrderedDict
import json

def MakeJson(bestPlan,Data):
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
			names.append(Data.NAMES[destination])
			latitudes.append(Data.COORDINATES[destination][0])
			longitudes.append(Data.COORDINATES[destination][1])
			start.append(bestPlan.pi[destination][i])
			end.append(bestPlan.pi[destination][i]+Data.SERVICETIME[destination])
			free.append(bestPlan.pi[destination][i]-bestPlan.a[destination][i])
		i=i+1

	response_data=OrderedDict()
	response_data["no_of_days"]=len(no_of_locations)
	response_data["no_of_locations"]=no_of_locations
	
	count=0
	
	plan_obj={}
	days=[]

	for i in range (len(no_of_locations)):
		location_list=[]
		location_obj={}
		for j in range (no_of_locations[i]):
			elements=OrderedDict()
			elements["locationId"]=locationId[count]
			elements["Name"]=names[count]
			elements["latitude"]=str(latitudes[count])
			elements["longitude"]=str(longitudes[count])
			elements["Start_time"]=str(start[count])
			elements["End_time"]=str(end[count])
			elements["Free_time"]=str(free[count])
			count=count+1
			location_list.append(elements)
		location_obj["location"]=location_list
		days.append(location_obj)
	plan_obj["Day"]=days
	response_data["Plan"]=plan_obj

	return json.dumps(response_data, indent=4, separators=(',', ': '))