# Create your views here.

from django.shortcuts import render

class Employee:
	def __init__ (self, name, address, age, email, birthday):
		self.name = name
		self.address = address
		self.age = age
		self.email = email
		self.birthday = birthday
def index(request):
	employee1 = Employee('Kyaw Kyaw', 'Kyeemyindine', 25, 'kyaw@gmail.com', '20-02-2022')
	employee2 = Employee('Aung Aung', 'Ahlone', 18, 'aung@gmail.com', '10-03-2022')
	employee3 = Employee('Mg Mg',    'Dagon',   34, 'mgmg@gmail.com', '10-03-1989')
	employees = [ employee1, employee2 ,employee3]
	context = { "employee_list": employees }
	return render(request, '7_index_ttagsextends.html', context)