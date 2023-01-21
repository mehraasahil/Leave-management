from django.shortcuts import render
from rest_framework import viewsets
from api.models import User,AddLeave,Empid
from api.serializer import UserSerializer,AddLeaveSerializer,EmpidSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class= UserSerializer


    # @action(detail=True,methods=['get'])
    # def employees(self,request,pk=None):
    #     company=Company.objects.get(pk=pk)
    #     emps=Employee.objects.filter(company=company)

    #     emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
    #     return Response(emps_serializer.data)

class AddLeaveViewSet(viewsets.ModelViewSet):
    queryset=AddLeave.objects.all()
    serializer_class= AddLeaveSerializer   

class EmpidViewset(viewsets.ModelViewSet):
    queryset=Empid.objects.all()
    serializer_class= EmpidSerializer    