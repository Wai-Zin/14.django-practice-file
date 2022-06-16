from django.urls import path
from model_form_app import views
urlpatterns = [
	path('show_model_form/', views.index),
	path('save_model_form/', views.save),
]