from django.shortcuts import render,redirect
from testapp.forms import EmployeeForm
from testapp.models import Employee
# Create your views here.
def display_view(request):
    emp_list=Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})

def insert_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('Validation error')
    return render(request,'testapp/insert.html',{'form':form})

def delete_view(request,id):
    record=Employee.objects.get(id=id)
    record.delete()
    return redirect('/')
    
def update_view(request,id):
    
    record=Employee.objects.get(id=id)
    form=EmployeeForm(instance=record)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=record)
        form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'form':form})
    
    