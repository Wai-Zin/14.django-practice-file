from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from hr_employees import models
from hr_employees import forms

from django.urls import reverse_lazy

from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.contrib.auth import logout

def logout_view(request):
	logout(request)
	return redirect('login')

class EmployeeListView(LoginRequiredMixin,ListView):
	login_url = reverse_lazy('login')
	model = models.EmployeeModel
	context_object_name = 'employees_list'
	template_name = 'employee_list.html'

class EmployeeCreateView(LoginRequiredMixin,CreateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("employee_list")
	model = models.EmployeeModel
	form_class = forms.EmployeeCreateForm
	template_name = 'employee_create.html'


class EmployeeUpdateView(SuperuserRequiredMixin, LoginRequiredMixin,UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("employee_list")
	model = models.EmployeeModel
	form_class = forms.EmployeeUpdateForm
	context_object_name = "employee"
	template_name = 'employee_update.html'

class EmployeeDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("employee_list")
	model = models.EmployeeModel
	context_object_name = "employee"
	template_name = 'employee_delete.html'

class EmployeeDetailView(LoginRequiredMixin, DetailView):
	login_url = reverse_lazy('login')
	model = models.EmployeeModel
	context_object_name = "employee"
	template_name = 'employee_detail.html'