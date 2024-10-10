from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound,HttpResponse
import json

# Create your views here.
def jsonConvert(request):
  return render(request,"jsonConvert.html")

data_store={}

def jsonConvert(request):
  if request.method=="POST":
    data = request.POST
    
    jsonInput=data.get('jsonInput')
    
    try:
      json_parsed = json.loads(jsonInput)
      url = data.get('url')
      endpoint = data.get('endpoint')
      fullUrl=f"{url.strip()}{endpoint.strip()}"
      request.session[endpoint] = jsonInput
      error_message=False 
    except json.JSONDecodeError:
      error_message="Invalid JSON format. Please provide valid JSON."
      fullUrl = None  
      url = ""  
      endpoint = ""
      
      
    
    
    
    # data_store[endpoint] = jsonInput
    
    
    context = {
      "url":url,
      "endpoint":endpoint,
      "jsonInput":jsonInput,
      "fullUrl":fullUrl,
      "error_message":error_message
    }
    
    return render(request,"jsonConvert.html",context)
  return render(request,"jsonConvert.html")

def show_json(request,endpoint):
  
  json_data = request.session.get(endpoint)
  if json_data:
    parsed_json = json.loads(json_data)
    
    return JsonResponse(parsed_json)
    
  else:
    return HttpResponseNotFound('No data found for this endpoint.')