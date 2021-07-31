from django.urls import path 
from . import views 


urlpatterns = [
    path('register/', views.register, name = 'register-main'),
    path('login/', views.login, name = 'login-main'),
    path('profile/', views.profile, name = 'profile-main'),
    path('logout/', views.logout, name = 'logout-main'),
    path('registerforevent/', views.registerforevent, name = 'eventregister-main'),
    path('sendemail/', views.sendthemail, name = 'emailsend-main'),
    


    
]