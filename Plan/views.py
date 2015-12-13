from django.shortcuts import render
from django.http import HttpResponse
from main import MakePlan
from make_json import MakeJson


from parameters_class import ParameterClass

def home(request):

	Parameters=ParameterClass(request)

	
	plan = MakePlan(Parameters)
	json = MakeJson(plan[0],plan[1])
	


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
	return HttpResponse(json,content_type="application/json")

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