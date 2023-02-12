from dataclasses import fields
from django import forms
from . models import Employee

class EmployeeFrom(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['emp_code','fname','mobile','position']
        labels={
            'fname':'Full Name',
            'emp_code':'Employee Code',
            'mobile':'Mobile No.',
            'position':'Position'
        }