from django.shortcuts import render
import requests
# Create your views here.
import os

from dotenv import load_dotenv

load_dotenv()

def weather_city(request):
    city = 0
    if request.method == "POST":
        city = request.POST['city']
    
    # Your OpenWeatherMap API Key
    api_key = os.getenv('API_KEY')
    
    # OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data_weather = response.json()

    if data_weather["cod"] != 200:
        weather_info = {"error": "City not found"}
    else:
        # استخراج بيانات الطقس المطلوبة
        weather_info = {
            "city": city,
            "temperature": data_weather["main"]["temp"],  # درجة الحرارة المئوية
            "humidity": data_weather["main"]["humidity"],  # الرطوبة
            "description": data_weather["weather"][0]["description"],  # وصف الطقس
            "wind_speed": data_weather["wind"]["speed"],  # سرعة الرياح
            "icon": f"http://openweathermap.org/img/wn/{data_weather['weather'][0]['icon']}@2x.png",  # رابط الأيقونة
            "data_weather": data_weather 
        }

    return render(request, "city/weather.html", {"weather": weather_info})


