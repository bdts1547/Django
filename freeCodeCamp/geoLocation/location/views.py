from django.shortcuts import render
from django.views import View
import requests
import json


# Create your views here.
class Home(View):
    def get(self, request):
        ip_res = requests.get("https://api.ipify.org?format=json")
        ip = json.loads(ip_res.text)
        res = requests.get(f"http://ip-api.com/json/{ip['ip']}")
        location_data = json.loads(res.text)
        

        return render(request, 'index.html', {'data': location_data})