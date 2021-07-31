from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth.models import User, auth 
from django.contrib.auth import authenticate, login 
from main.models import events
from django.http import HttpResponse, HttpRequest
from django import forms
from django.shortcuts import render
from paspresente.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

import random
import string



def sendthemail(request):
    

    if request.method == 'POST':
        messagename = request.POST['message-name']
        messageemail = request.POST['message-email']
        message = request.POST['message']
        

        send_mail(
            'Query',
            "Name - \t " + messagename + "\n\nQuestion -  " + message,
            messageemail,
           ['timelapsernr@gmail.com']
        )
        return HttpResponse('Email Sent!')

    else:

        return render(request, "main/home.html", {})





def login(request) : 
    
    if request.method == 'POST' : 
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate( username = username, password = password)
        
        if user is not None :

            auth.login(request, user)

            messages.success(request, f'Welcome {username}')
            return redirect('profile-main')
        else : 
            err = "Wrong Credentials"
            return render(request , 'users/login.html', {'erroristhere' : err})
            
    else :
        return render(request, 'users/login.html')

def register(request): 
    if request.method == 'POST' : 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 : 
            if User.objects.filter(username = username).exists() :
                messages.warning(request, 'Account Exists')
                return redirect('register-main')

            else : 
                user = User.objects.create_user(username= username, password = password1, email= email, first_name= first_name, last_name = last_name)
                user.save()
                messages.success(request, f'Account created for {first_name}!. Login to continue')
                return redirect('login-main')
        else : 
            messages.warning(request, 'Password not matching')
            return redirect('register-main')
    else : 
        return render(request, 'users/register.html')



def profile(request : HttpRequest) : 
    userevent = events.objects.filter(username = 'akshathraghav', email = 'akshathraghav.r@gmail.com').first()
    username = request.user.username
    email = request.user.email
    userschosenevent = events.objects.filter(username=username, email=email).first()
    return render(request, 'users/profile.html', {'userevent' : userevent, 'username' : username, 'email' : email, 'userschosenevent' : userschosenevent})

def registerforevent(request) : 
    username = request.user.username
    email = request.user.email


    if request.method == 'POST' : 
        number = request.POST['number']
        schoolname = request.POST['schoolname']
        grade = request.POST['grade']
        section = request.POST['section']
        event1 = request.POST['event1']
        event2 = request.POST['event2']
        event3 = request.POST['event3']
        letters = string.ascii_letters
        code =  ''.join(random.choice(letters) for i in range(10)) 
        send_mail(
            'Query',
            "Discord - \t " + username + "\n\nSchoolName/Grade/Section - " + schoolname + " " + grade + section + "\n\nEvents  -  " + event1 + " " + event2 + " " + event3 + "\n\nRegistration Code : " + code,
            email,
        ['timelapsernr@gmail.com']
        )
        userevent1 = events.objects.create(username = username, email = email,   e1 = event1, e2 = event2, e3 = event3,      grade = grade, number = number,schoolname = schoolname ,section = section , code = code )
        userevent1.save()
        userschosenevent = events.objects.filter(username = username, email = email).first()

        return redirect('profile-main')
    else:
        userschosenevent = events.objects.filter(username=username, email=email).first()
        return render(request, 'users/registerforevent.html', { 'username' : username, "userchosenevent" : userschosenevent})


def logout(request) : 
    auth.logout(request)
    return redirect('main-home')

    