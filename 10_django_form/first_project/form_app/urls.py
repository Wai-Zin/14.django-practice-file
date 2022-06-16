from django.urls import path
from form_app import views

urlpatterns = [
	path('create_form/', views.index),
]