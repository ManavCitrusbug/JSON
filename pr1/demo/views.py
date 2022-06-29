
from calendar import c
from multiprocessing import Value
from re import T
from turtle import home
from django.http import JsonResponse
from django.shortcuts import render
from pr1.settings import BASE_DIR
from django.views import *
import json
# import requests
# Create your views here.
# import requests
import urllib.request, json 
class Country(View):
    def get(self,request):
            url='http://127.0.0.1:8000/countries/'
            with urllib.request.urlopen(f"{url}") as url:
             data = json.loads(url.read().decode())
            return render(request,'demo.html',{'data':data})


class ListCountries(View):
    def get(self, request):
        url='http://127.0.0.1:8000/static/json/countries.json/'
        with urllib.request.urlopen(f"{url}") as url:
            data = json.loads(url.read().decode())
          
        return JsonResponse(data=data,safe=False)

class ListState(View):
    def get(self, request):
        data1=[]
        val=0
        country=request.GET['country']
    
        url='http://127.0.0.1:8000/static/json/states.json/'
        with urllib.request.urlopen(f"{url}") as url:
            data = json.loads(url.read().decode())
            for i in data:
               if i['country_name']==country:
                    data1.append(i['name'])
        return JsonResponse({"data1":data1})
        # else:
        #     return JsonResponse({"val":val})

class ListCity(View):
    def get(self, request):
        state=[]
        states=request.GET['states']
        url='http://127.0.0.1:8000/static/json/cities.json/'
        with urllib.request.urlopen(f"{url}") as url:
            data = json.loads(url.read().decode())
            for i in data:
               if i['state_name']==states:
                    state.append(i['name'])
        return JsonResponse({"data1":state})


               
                    
                    


                    



