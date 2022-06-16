# Create your views here.
from django.http import HttpResponse
from calendar import HTMLCalendar
def index(request):
	cal = HTMLCalendar().formatmonth(2022, 2)
	return HttpResponse(cal)