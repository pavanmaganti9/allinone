# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeeSerializer

# Create your views here.
class employeelist(APIView):

	def get(self, request):
		empdata = employees.objects.all()
		serializer = employeeSerializer(empdata, many = True)
		return Response(serializer.data)
		
	def post(self):
		passs