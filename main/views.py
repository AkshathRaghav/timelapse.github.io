from django.shortcuts import render
from django.http import HttpResponse
from .models import test

# Create your views here.
#this will store the http requests


def home(request ) :
    return render(request, "main/home.html") 
    
def cubing(request ) :
    return render(request, "main/cubing.html") 

def art(request ) :
    return render(request, "main/art.html") 

def battleofbands(request ) :
    return render(request, "main/battleofthebands.html") 

def poetry(request ) :
    return render(request, "main/poetry.html") 

def hackathon(request ) :
    return render(request, "main/hackathon.html") 

def fashion(request ) :
    return render(request, "main/fashion.html")
    
def debate(request ) :
    return render(request, "main/debattle.html") 

def meme(request ) :
    return render(request, "main/meme.html")
    
def dance(request ) :
    return render(request, "main/dance.html") 

    
def gaming(request ) :
    return render(request, "main/gaming.html")
def photo(request ) :
    return render(request, "main/photo.html") 