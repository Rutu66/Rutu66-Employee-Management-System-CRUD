from django.shortcuts import render, redirect
from .models import *
from django .contrib import messages

# Create your views here.

def index(request):
    emp = employee.objects.all()
    data = {
        'emp': emp
    }
    
    return render(request, 'index.html',data)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        salary = request.POST.get('salary')
        
        emp = employee(first_name=first_name,last_name=last_name,salary=salary)
        emp.save()
        messages.success(request,"added successfully")
        return redirect("index")
        
    
    return render(request, 'add_employee.html')

def remove_emp(request,emp_id):
    emp = employee.objects.get(id=emp_id)
    emp.delete()
    messages.success(request,"delete successfully")
    return redirect("index")
    
    
    return render(request, 'remove_emp  .html')

def update_emp(request,emp_id):
    emp = employee.objects.get(id=emp_id)
    
    if request.method=="POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        salary = request.POST.get('salary')
        
        emp=employee.objects.filter(id=emp_id).update(first_name=first_name,last_name=last_name,salary=salary)
        messages.success(request,"update successfully")
        return redirect("index")
    data = {
        'emp':emp
    }
    return render(request, 'update_employee.html',data)