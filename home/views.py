from django.shortcuts import redirect, render
from home.models import Employee
from .forms import EmployeeFrom

# Create your views here.
def employee_list(request):
    list=Employee.objects.all()
    return render(request,'emp_list.html',{'list':list})

def employee_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeFrom()
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeFrom(instance=employee)
        return render(request,'emp_form.html',{'form':form})
    else:
        form = EmployeeFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list/')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')


