from django.shortcuts import render
import json
from django.http import HttpResponse
from main import make_plan
from collections import OrderedDict



def home(request):

    
    
    city=request.GET['city']
    days=int(request.GET['days'])
    start=int(request.GET['Start_time'])
    end=int(request.GET['End_time'])
    budget=int(request.GET['budget'])
    
    response = make_plan(city,days,start,end,budget)
    
    response_data=OrderedDict()
    response_data["no_of_days"]=len(response[0])
    response_data["no_of_locations"]=response[0]
    
    count=0
    
    plan_obj={}
    days=[]

    for i in range (len(response[0])):
        location_list=[]
        location_obj={}
        for j in range (response[0][i]):
            elements=OrderedDict()
            elements["Name"]=response[1][count]
            elements["latitude"]=str(response[2][count])
            elements["longitude"]=str(response[3][count])
            elements["Start_time"]=str(response[4][count])
            elements["End_time"]=str(response[5][count])
            elements["Free_time"]=str(response[6][count])
            count=count+1
            location_list.append(elements)
        location_obj["location"]=location_list
        days.append(location_obj)
    plan_obj["Day"]=days
    response_data["Plan"]=plan_obj


    #for i in range (len(response[0])):
    #    response_data['Plan'][day + str(i+1)]=OrderedDict()
    #    for j in range (response[0][i]):
    #        response_data['Plan'][day + str(i+1)][location + str(j+1)]=OrderedDict()
    #    for j in range (response[0][i]):
    #        response_data['Plan'][day + str(i+1)][location + str(j+1)]["Name"]=response[1][count]
    #        response_data['Plan'][day + str(i+1)][location + str(j+1)]["latitude"]=str(response[2][count])
    #        response_data['Plan'][day + str(i+1)][location + str(j+1)]["longitude"]=str(response[3][count])
    #        response_data['Plan'][day + str(i+1)][location + str(j+1)]["Start_time"]=str(response[4][count])
    #        response_data['Plan'][day + str(i+1)][location + str(j+1)]["End_time"]=str(response[5][count])
    #        response_data['Plan'][day + str(i+1)][location + str(j+1)]["Free_time"]=str(response[6][count])
    #        count=count+1
    return HttpResponse(json.dumps(response_data, indent=4, separators=(',', ': ')),content_type="application/json")

# Create your views here.
#day1 = []
 #   day1.append([1,2])
  #  day1.append([1,2])
   # day1.append([1,2])
    #day1.append([1,2])
    #day1.append([1,2])

    #day = "day"
    #i=1

    #response_data['Result'] = {}
    #response_data['Result'][day + str(i)] = day1
    #i=i+1

    #day2 = []
    #day2.append([1,2])
    #day2.append([1,2])
    #day2.append([1,2])
    
    #response_data['Result'][day + str(i)] = day2