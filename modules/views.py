# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NameForm
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeeSerializer


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
	
def post(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
		  return HttpResponseRedirect('index')
    # if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()
	return render(request, 'form.html', {'form': form,'title' : 'Forms'})
	
def pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here
    p.drawString(100, 100, 'Hello world.')
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
	
def get(request):
	empdata = employees.objects.all()
	serializer = employeeSerializer(empdata, many = True)
	return Response(serializer.data)	
	
class employeelist(APIView):

	def get(self, request):
		empdata = employees.objects.all()
		serializer = employeeSerializer(empdata, many = True)
		return Response(serializer.data)
		
	def post(self):
		passs