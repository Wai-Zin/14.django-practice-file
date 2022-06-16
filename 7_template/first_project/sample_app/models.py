from django.db import models
from django.utils import timezone
# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=20)
	address = models.TextField(max_length=50)

	age = models.IntegerField("Age", default=0)
	email = models.EmailField(max_length=50, default='test@gmail.com')
	birthday = models.DateField("Birthday", default=timezone.now)
	image = models.ImageField("Image", default=None)
		

