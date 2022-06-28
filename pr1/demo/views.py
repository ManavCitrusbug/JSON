
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
class Home(View):

    def get(self,request):
            url='http://127.0.0.1:8000/static/json/countries.json/'
            with urllib.request.urlopen(f"{url}") as url:
             data = json.loads(url.read().decode())
            # print(type(data[0]))
            return render(request,'demo.html',{'data':data})


class ListCountries(View):
    def get(self, request):
        url='http://127.0.0.1:8000/static/json/countries.json/'
        with urllib.request.urlopen(f"{url}") as url:
            data = json.loads(url.read().decode())
          
        return JsonResponse(data=data,safe=False)

class ListState(View):
    def get(self, request):
        url='http://127.0.0.1:8000/static/json/states.json/'
        with urllib.request.urlopen(f"{url}") as url:
            data = json.loads(url.read().decode())
            
        return JsonResponse(data=data,safe=False)

class ListCity(View):
    def get(self, request):
        url='http://127.0.0.1:8000/static/json/cities.json/'
        with urllib.request.urlopen(f"{url}") as url:
            data = json.loads(url.read().decode())
           
        return JsonResponse(data=data,safe=False)

class FilterState(View):
     def get(self, request):
        country=request.GET['country']
        print(country)
        return render(request,'demo.html')
        # state=[]
        # url='http://127.0.0.1:8000/static/json/states.json/'
        # with urllib.request.urlopen(f"{url}") as url:
        #     data = json.loads(url.read().decode())
        #     countryname=json.loads(country)
        #     for i in data:
        #         if countryname == i['country_name']:
                    
               
                    
                    


                    



