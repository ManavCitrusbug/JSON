
from calendar import c
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
    list=[]
    def name(self,data):
        print(data)
        self.data1=data

        for i in self.data1:
            list.append(i.name)
  
    def get(self,request):
        
        # url='http://127.0.0.1:8000/static/json/states.json'
        # with urllib.request.urlopen(f"{url}") as url:
        #     data = json.loads(url.read().decode())
        #     print(data)
        return render(request,'demo.html')


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
            print(data)
        return JsonResponse(data=data,safe=False)

class ListCity(View):
    def get(self, request):
        url='http://127.0.0.1:8000/static/json/cities.json/'
        with urllib.request.urlopen(f"{url}") as url:
            data = json.loads(url.read().decode())
           
        return JsonResponse(data=data,safe=False)

