from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=240)
    rollnum=models.CharField(max_length=20)
    course=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}Student'
