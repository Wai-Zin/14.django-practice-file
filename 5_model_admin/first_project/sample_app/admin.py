from django.contrib import admin

# Register your models here.
from .models import Employee
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['name','address','age','email','birthday','image']

admin.site.register(Employee,EmployeeAdmin)
		