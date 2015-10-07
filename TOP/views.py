from django.shortcuts import render
import json
from django.http import HttpResponse
from main import plan


def home(request):
    response_data={}
    days=request.GET['days']
    response_data['Result'] = plan(int(days)).tolist()
    return HttpResponse(json.dumps(response_data),content_type="application/json")

# Create your views here.
