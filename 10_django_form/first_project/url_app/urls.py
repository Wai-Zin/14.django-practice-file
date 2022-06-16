from django.urls import path
from url_app import views
urlpatterns = [
	path('get_employee/<int:employee_id>', views.get_employee),
]