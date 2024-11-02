from django.shortcuts import render
import urllib.request
import json

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=7defe7da8db6d4b4f50f062469f628de').read()
        json_data = json.loads(res)
        data = {
            'country_code': str(json_data['sys']['country']),
            'max_temp': str(json_data['main']['temp_max'])+' k' ,
            'min_temp': str(json_data['main']['temp_min'])+' k' ,
            'coordinates': str(json_data['coord']['lon'])+'   '+str(json_data['coord']['lat']),
            'temperature': str(json_data['main']['temp'])+' k',
            'pressure':str(json_data['main']['pressure'])+' hPa',
            'humidity':str(json_data['main']['humidity'])+'%',
        }
    else:
        city=''
        data = {}
    return render(request, 'index.html', {'city':city.capitalize(),'data':data})
    

