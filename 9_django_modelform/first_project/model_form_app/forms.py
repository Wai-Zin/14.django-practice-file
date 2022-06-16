from django import forms
from sample_app import models

class EmployeeForm(forms.ModelForm):

	class Meta:
		model = models.Employee
		fields = "__all__"