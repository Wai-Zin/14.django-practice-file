from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse
from sample_app import models
def get_employee(request, employee_id):
	employee = models.Employee.objects.get(id=employee_id)
	name = employee.name
	return HttpResponse(name)
