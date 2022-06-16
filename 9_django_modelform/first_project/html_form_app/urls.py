from django.urls import path
from html_form_app import views
urlpatterns = [
	path('show_html_form/', views.index),
	path('save_html_form/', views.save),
]