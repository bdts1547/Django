from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import urllib.request
import json


# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    

    def post(self, request):
        city = request.POST['city']
        api_key_weather = None
        if not api_key_weather:
            assert False
        res = urllib.request.urlopen('http://api.openweathermap.url/data/2.5/weather?q{}&appid={}'.format(city, api_key_weather)).read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['sys']['pressure']),
            "humidity": str(json_data['sys']['humidity']),

        }
        return render(request, 'index.html', data)
