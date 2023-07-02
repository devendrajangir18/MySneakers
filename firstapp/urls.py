from django.contrib import admin
from django.urls import path 
from firstapp import views 
 
# index = function name hai jo views mai banega
# home = ye path ka name hai jo url mai dalega

urlpatterns = [
    path('', views.index, name="home" ),
    path('about', views.about, name="about"),
    path('service', views.service, name="service"),
    path('contact', views.contact, name="contact")
]