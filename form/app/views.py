from django.shortcuts import render,redirect
from app.forms import StudentForm
from .models import Student
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    res = StudentForm(label_suffix=' :- ',initial={'email':'@gmail.com'}
                                 ,auto_id='%s')
    return render(request,'index.html',{'form':res})

def reg(request):
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            cn = fm.cleaned_data['contact']
            em = fm.cleaned_data['email']
            pw = make_password(fm.cleaned_data['password'])
            Student(name=nm,contact=cn,email=em,password=pw).save()
            return redirect('/table/')
        
def table(request):
     data = Student.objects.all()
     return render(request,'table.html',{'data':data})

def delete(request,uid):
     Student(id=uid).delete()
     return redirect('/table/')

def edit(request,uid):
        res = StudentForm()
        uid = uid
        return render(request,'edit.html',{'uid':uid,'form':res})

def update(request):
        fm = StudentForm(request.POST)
        if fm.is_valid():
                uid = request.POST['hide']
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['email']
                pw = make_password(fm.cleaned_data['password'])
                cn = fm.cleaned_data['contact']
                Student(id=uid,name=nm,contact=cn,email=em,password=pw).save()
                return redirect('/table/')

