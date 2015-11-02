from django.shortcuts import render
import json
from django.http import HttpResponse
from main import OptiPath
from collections import OrderedDict
import numpy as np

# Create your views here.
def home(request):
	number=int(request.GET['number'])
	coordinates=np.zeros((number,2))
	for i in range (number):
		x='x'+str(i)
		y='y'+str(i)
		coordinates[i][0]=int(request.GET[x])
		coordinates[i][1]=int(request.GET[y])
	response=OptiPath(coordinates)

	response_data=OrderedDict()
	response_data["GreedyDistance"]=response[0][0]
	response_data["GreedyPath"]=response[0][1].tolist()
	response_data["Opt2Distance"]=response[1][0]
	response_data["Opt2Path"]=response[1][1].tolist()

	return HttpResponse(json.dumps(response_data, indent=4, separators=(',', ': ')),content_type="application/json")

