from django.shortcuts import render
from django.http  import JsonResponse
from .models import people
import requests
from .forms import inputField

# Create your views here.

def webpage(request):
    resource = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data = resource.json()
    context = {"dataset":data}

    return render(request,'web2.html',context)

def name(request):
    
    details = people.objects.all()
    context = {"dataset":details}

    return render(request,'web.html',context)

def get_weather(request):
    weather_data = {}

    if request.method == 'POST':
        form = inputField(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['cityName']
            API_key = '5590b76932c64b6383193cdc891c5e5d'
            api_url = f'https://api.weatherbit.io/v2.0/current?city={city_name}&country=India&key={API_key}'
            
            try:
                response = requests.get(api_url)
                print(response.status_code)
                weather_data = response.json()
            except Exception as e:
                print(f"Error fetching weather data: {e}")
                weather_data = {}
    else:
        form = inputField()

    context = {'data': weather_data, 'form': form}
    return render(request, 'weather_template.html', context)