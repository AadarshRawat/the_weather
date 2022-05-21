from django.shortcuts import render
import requests
from django.contrib.messages import constants as messages

def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a0090e29c1ae20b4a3a1cb8c06ebe3d8'
    if 'city' in request.GET:
        city=request.GET.get('city')
        r = requests.get(url.format(city)).json()

        if r['cod']=='404' or r['cod']=='400':

            return render(request,'weather/index.html')
        else:

            city_weather = {
                'city':r['name'],
                'temperature': r['main']['temp'],
                'max': r['main']['temp_max'],
                'min': r['main']['temp_min'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            context={'city_weather':city_weather}
            return render(request,'weather/index.html',context)
    else:
        return render(request, 'weather/index.html')


    # print(city_weather)

