from django.urls import path
from hr_employees import views

urlpatterns = [
	path('logout/', views.logout_view, name='logout'),

	path('show_employee/', views.EmployeeListView.as_view(), name='employee_list'),
	path('new_employee/', views.EmployeeCreateView.as_view(), name='employee_create'),
	path('<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),
	path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
	path('<int:pk>', views.EmployeeDetailView.as_view(), name='employee_detail')
]