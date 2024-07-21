from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from api.models import Employee

from api.serializers import EmployeeSerializer

class EmployeeViewSetView(viewsets.ModelViewSet):

    serializer_class=EmployeeSerializer

    queryset=Employee.objects.all()


