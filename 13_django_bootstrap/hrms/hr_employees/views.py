from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from hr_employees import models
from hr_employees import forms

from django.urls import reverse_lazy

class EmployeeListView(ListView):
	model = models.EmployeeModel
	context_object_name = 'employees_list'
	template_name = 'employee_list.html'

class EmployeeCreateView(CreateView):
	success_url = reverse_lazy("employee_list")
	model = models.EmployeeModel
	form_class = forms.EmployeeCreateForm
	template_name = 'employee_create.html'


class EmployeeUpdateView(UpdateView):
	success_url = reverse_lazy("employee_list")
	model = models.EmployeeModel
	form_class = forms.EmployeeUpdateForm
	context_object_name = "employee"
	template_name = 'employee_update.html'

class EmployeeDeleteView(DeleteView):
	success_url = reverse_lazy("employee_list")
	model = models.EmployeeModel
	context_object_name = "employee"
	template_name = 'employee_delete.html'

class EmployeeDetailView(DetailView):
	model = models.EmployeeModel
	context_object_name = "employee"
	template_name = 'employee_detail.html'