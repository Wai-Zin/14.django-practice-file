from django import forms
from hr_employees import models

class EmployeeCreateForm(forms.ModelForm):
	class Meta:
		model = models.EmployeeModel
		fields = '__all__'


class EmployeeUpdateForm(forms.ModelForm):
	class Meta:
		model = models.EmployeeModel
		fields = '__all__'