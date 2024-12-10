from django.shortcuts import render,redirect
from crudapp_forms.models import employee
from crudapp_forms.forms import employeeforms
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def add(request):
    form=employeeforms()
    return render(request,"add_employee.html",{'form':form})

def addemp(request):
    if request.method == 'POST':
        form = employeeforms(request.POST)
        if form.is_valid():
            form.save()
            subject="Registration"
            message="We have received application"
            recipient=form.cleaned_data.get('emp_email')
            send_mail(subject,message,settings.EMAIL_HOST_USER,['manjusham92@gmail.com'])
            return redirect('show')
    return render(request,"add_employee.html")

def show(request):
    empls=employee.objects.all()
    return render(request,"show_employee.html",{'empls':empls})

def update(request,id):
    empl=employee.objects.get(id=id)
    form=employeeforms(instance=empl)
    if request.method == 'POST':
        form=employeeforms(request.POST,instance=empl)
        if form.is_valid():
            form.save()
            return redirect('show')
    return render(request,'update.html',{'form':form})

def delete(request,id):
    emp = employee.objects.get(id=id)
    emp.delete()
    return redirect('show')
