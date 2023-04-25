from django.urls import path,include
from .import views

urlpatterns =[
    path('',views.index, name="index"),
    path('Admissions',views.Admissions, name="Admissions"),
    path('contact', views.contacts, name="contact"),
    path('Events', views.event, name="event"),
    path('News', views.news, name="news"),

]
