from django.contrib import admin
from django.urls import path
from . import views
app_name = "classroom"


urlpatterns = [
    path('<slug:slug>/', views.classno,name="classno"),

]
