from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.home, name = 'main-home'),
    path('events/art/', views.art, name = 'art'),
    path('events/battleofthebands/', views.battleofbands, name = 'battleofthebands'),
    path('events/cubing/', views.cubing, name='cubing'),
    path('events/poetry/', views.poetry, name='poetry'),
    path('events/hackathon/', views.hackathon, name = 'hackathon'),
    path('events/fashion/', views.fashion, name='fashion'),
    path('events/debate/', views.debate, name='debate'),
    path('events/gaming/', views.gaming, name = 'gaming'),
    path('events/dance/', views.dance, name='dance'),
    path('events/meme/', views.meme, name='meme'),
    path('events/photo/', views.photo, name = 'photo'),
    
    
    
    
    
]