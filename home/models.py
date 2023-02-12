from turtle import position
from django.db import models

# Create your models here.

class Position(models.Model):
    title=models.CharField(max_length=25)
    def __str__(self) -> str:
        return self.title
    
class Employee(models.Model):
    fname=models.CharField(max_length=25)
    emp_code=models.CharField(unique=True,max_length=3)
    mobile=models.CharField(max_length=10)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.fname