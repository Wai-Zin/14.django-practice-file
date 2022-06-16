from django.shortcuts import render,redirect

# Create your views here.
# Create your views here.
from sample_app import models
def index(request):
	employee = models.Employee()
	return render(request,"index_html_form.html", {'employee': employee})
def save(request):
	if request.method == "POST":
		name = request.POST.get('name')
		address = request.POST.get('address')
		age = request.POST.get('age')
		email = request.POST.get('email')
		birthday = request.POST.get('birthday')
		image = request.POST.get('image')
		employee = models.Employee.objects.create(
		name=name,
		address=address,
		age=age,
		email=email,
		birthday=birthday,
		image=image
		)
		employee.save()
		return redirect('/html_form_app/show_html_form')
	else:
		employee = models.Employee()
