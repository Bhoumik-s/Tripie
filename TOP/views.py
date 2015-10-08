from django.shortcuts import render
import json
from django.http import HttpResponse
from main import plan
from collections import OrderedDict



def home(request):

    response_data=OrderedDict()
    response_data['Plan']=OrderedDict()
    
    city=request.GET['city']
    days=int(request.GET['days'])
    start=int(request.GET['Start_time'])
    end=int(request.GET['End_time'])
    budget=int(request.GET['budget'])
    
    response = plan(city,days,start,end,budget)
    count=0
    day = "day"
    location="location"
    for i in range (len(response[0])):
        response_data['Plan'][day + str(i+1)]=OrderedDict()
        for j in range (response[0][i]):
            response_data['Plan'][day + str(i+1)][location + str(j+1)]=OrderedDict()
        for j in range (response[0][i]):
            response_data['Plan'][day + str(i+1)][location + str(j+1)]["Name"]=response[1][count]
            response_data['Plan'][day + str(i+1)][location + str(j+1)]["latitude"]=str(response[2][count])
            response_data['Plan'][day + str(i+1)][location + str(j+1)]["longitude"]=str(response[3][count])
            response_data['Plan'][day + str(i+1)][location + str(j+1)]["Start_time"]=str(response[4][count])
            response_data['Plan'][day + str(i+1)][location + str(j+1)]["End_time"]=str(response[5][count])
            response_data['Plan'][day + str(i+1)][location + str(j+1)]["Free_time"]=str(response[6][count])
            count=count+1
    return HttpResponse(json.dumps(response_data),content_type="application/json")

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