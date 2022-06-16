
from django.shortcuts import render

def index(request):
	employees = ['Kyaw Kyaw', 'Aung Aung', 'Mg Mg', 'Aye Aye']
	return render(request,'4_index_ttagsfor.html',{ "employee_list": employees })