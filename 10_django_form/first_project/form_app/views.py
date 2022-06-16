from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from form_app import forms

def index(request):
	if request.method == "POST":
		form = forms.ContactForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			message = "Hello " + username
			return HttpResponse(message)
	else:
		form = forms.ContactForm()
	return render(request,"contact_form.html", { 'form': form })