from django.shortcuts import render
from django.http import HttpResponse
from main import MakePlan
from make_json import MakeJson


from parameters_class import ParameterClass

def home(request):

	Parameters=ParameterClass(request)

	
	plan = MakePlan(Parameters)
	json = MakeJson(plan[0],plan[1],Parameters)

	


	
	return HttpResponse(json,content_type="application/json")

