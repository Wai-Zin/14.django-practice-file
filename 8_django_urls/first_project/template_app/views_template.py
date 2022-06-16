# Create your views here.
from django.http import HttpResponse
from django.template import loader
def index(request):
	print('index call me')
	template = loader.get_template('1_index_template.html')
	return HttpResponse(template.render())