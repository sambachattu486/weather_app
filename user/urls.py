from django.urls import path
from .views import webpage,name,get_weather
urlpatterns = [
    path('posts/',webpage),
    path('name/',name),
    path('',get_weather,name='get_weather')
]