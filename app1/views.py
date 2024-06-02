from django.shortcuts import render,redirect

from .forms import RegisterForm
from .models import EmployeeModel
# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/getdata/')
    form=RegisterForm()
    return render(request,'register.html',{'form':form})

def getdata(request):
    data=EmployeeModel.objects.all()
    return render(request,'data.html',{'data':data})

