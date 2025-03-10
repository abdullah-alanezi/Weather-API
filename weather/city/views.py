from django.shortcuts import render
import requests
# Create your views here.

def weather_city(request):
    city = "Hail"
    if request.method == "POST":
        city = request.POST['city']
    
    url = f"https://wttr.in/{city}?format=j1"
    
    response = requests.get(url)
    data_weather = response.json()

    # استخراج بيانات الطقس المطلوبة
    current_condition = data_weather["current_condition"][0]  # الطقس الحالي
    weather_info = {
        "city": city,
        "temperature": current_condition["temp_C"],  # درجة الحرارة المئوية
        "humidity": current_condition["humidity"],  # الرطوبة
        "description": current_condition["weatherDesc"][0]["value"],  # وصف الطقس
        "wind_speed": current_condition["windspeedKmph"],
        "icon": current_condition["weatherIconUrl"][0]["value"],  # رابط الأيقونة
        "data_weather": data_weather 
    }


    return render(request, "city/weather.html", {"weather": weather_info})

