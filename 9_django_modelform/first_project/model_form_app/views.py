from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from model_form_app import forms
from sample_app import models

def index(request):
	form = forms.EmployeeForm()
	return render(request, "index_model_form.html", { 'form': form })
def save(request):
	if request.method == "POST":
		form = forms.EmployeeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/model_form_app/show_model_form')
	else:
		form = forms.EmployeeForm()
	return render(request,"index_model_form.html", { 'form': form })
