# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('2_index_tvariable.html')
	employee = {
		'name': 'Aung Aung',
		'age' : '25',
		'address': 'Yangon'
	}
	return HttpResponse(template.render(employee))