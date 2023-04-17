from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from models import Departments,Employees
from serializers import DepartmentSerializer,EmployeeSerializer

@csrf_exempt
def departmentApi(request,id=0):
     if request.method=='GET':
         departments=Departments.objects.all()
         departments_serializer=DepartmentSerializer(departments,many=True)
         return JsonResponse(departments_serializer.data,safe=False )
     elif request.method=='POST':
         department_data=JSONParser().parse(request)
         departments_serializer=DepartmentSerializer(data=department_data)
         if departments_serializer.is_valid():
             departments_serializer.save()
             return JsonResponse('Added Successfully',safe=False)
         return JsonResponse('Failed to Add',safe=False)








