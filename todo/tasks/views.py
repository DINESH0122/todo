from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    tasks=Task.objects.all()
    form=Taskform()
    
    if request.method=='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks,'form':form}
    return render(request,'list.html',context)
 

def UpdateTask(request,pk):
    task=Task.objects.get(id=pk)
    form=Taskform(instance=task)
    if request.method=='POST':
        form=Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'form':form}
    return render(request,'update_task.html',context)

def deleteTask(request,pk):
    item=Task.objects.get(id=pk)
    if request.method=='POST':
         item.delete()
         return redirect('/')
    context={'item':item}
    return render(request,'delete.html',context)

