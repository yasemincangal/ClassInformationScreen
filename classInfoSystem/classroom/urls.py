from django.urls import path
from . import views
app_name = "classroom"


urlpatterns = [
    path('', views.classpick,name="home"),
    path('about/<str:pk_test>/',views.about,name="about"),
    
#    path('<slug:slug>/', views.classscreen),
#    path('<slug:slug>/', views.classscreen),

]
