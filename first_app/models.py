from django.db import models
from django.forms import CharField
from django.core.validators import MaxValueValidator

# Create your models here.
class course(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    year=models.PositiveIntegerField(validators=[MaxValueValidator(4)], default='1')
    mobile=models.PositiveIntegerField(validators=[MaxValueValidator(10000000000)], default='0')
    email=models.EmailField(max_length=264, default='NULL')
    course_name=models.CharField(max_length=100, default='NA')
    course_desc=models.TextField(default='NA')