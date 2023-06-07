from django.shortcuts import render, HttpResponse
from .models import EmployeeDetails,Role,Department
from datetime import datetime
from django.db.models import  Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')

def view_all_emp(request):
    emps=EmployeeDetails.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request, 'view_all_emp.html',context)

def add_emp(request):

    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        new_emp=EmployeeDetails(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hire_date=datetime.now() )
        new_emp.save()
        return HttpResponse( "Employee added successfuly")
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception occured! employee has not be added")


def remove_emp(request , emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=EmployeeDetails.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee successfully removed")
        except:
            return HttpResponse("Please Enter a valid id")
    emps=EmployeeDetails.objects.all()
    context={
        'emps':emps
    }
    return render(request, 'remove_emp.html',context)
    return render(request, 'remove_emp.html')

def filter_emp(request):
    if request.method =='POST':
        name=request.POST['first_name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=EmployeeDetails.objects.all()
        if name: 
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name ))
        if dept:
            emps=emps.filter(dept__name__icontains= dept)
        if role:
            emps=emps.filter(role__name__icontains= role)

        context={
        'emps':emps
    }
        return render(request, 'view_all_emp.html',context)

    elif request.method=='GET':
            return render(request, 'filter_emp.html')
    else:
            return HttpResponse("An exception occured")

        
    return render(request, 'filter_emp.html')