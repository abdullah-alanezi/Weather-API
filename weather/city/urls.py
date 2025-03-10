from django.urls import path
from .import views


app_name = "city"

urlpatterns = [
    path("",views.weather_city,name="weather_city")
    
]