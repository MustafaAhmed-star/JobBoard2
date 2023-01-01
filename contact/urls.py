from django.contrib import admin
from django.urls import path
from . import views

app_name = "contact"
 

 
urlpatterns = [
    path('',views.send_message,name="send_message"),
   
]
