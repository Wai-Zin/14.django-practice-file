# Create your views here.
from django.http import HttpResponse
from django.template import loader
def index(request):
	template = loader.get_template('3_index_ttagsif.html')
	employee = {
		'name':'Aung Aung',
		'address': 'Yangon',
		'age': 25
	}
	return HttpResponse(template.render(employee))