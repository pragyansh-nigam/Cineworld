from django.shortcuts import render, redirect
from django.conf import settings

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint

def home(req):
	return render(req,"home.html")

def swades(req):
	return render(req,"swades.html")

def tdk(req):
	return render(req,"tdk.html")

def got(req):
	return render(req,"got.html")

def cast(req):
	return render(req,"cast.html")

def signup(request):
	name = request.POST.get('name')
	mail = request.POST.get('mail')
	pwd = request.POST.get('pwd')
	query = "insert into signup(name,mail,password) value('{0}','{1}','{2}')".format(name,mail,pwd)
	cnn = settings.CONNECTION()
	cr = cnn.cursor()
	cr.execute(query)
	cnn.commit()
	msg = "Sign Up Success!"
	return render(request,"signup.html",{"msg":msg})

def login(request):
	return render(request,'login.html')