# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def index(request):
	#return HttpResponse('Hello Pavan!')
	return render(request, 'index.html', {'title' : 'Home'})
	
def success(request):
	return render(request, 'success.html', {'title' : 'Success'})
	
def email(request):
    subject = 'Thank you for registering'
    message = ' Dummy mail from Pavan.Maganti thanks '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['pavanmaganti9@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('success')