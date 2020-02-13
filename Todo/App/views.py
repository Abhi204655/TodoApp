from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import Taskform

# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        check = request.POST.get('check')
        print(check)
        task = Task()
        task.title = title
        if check == None:
            task.completed = False
            task.save()
        else:
            task.completed = True
            task.save()
        return redirect('/')
    else:
        tasks = Task.objects.all()
        return render(request,'App/base.html',{'tasks':tasks})

def delete(request,id):
    task = Task.objects.get(id = id)
    task.delete()
    return redirect('/')


def completed(request,id):
    task = Task.objects.get(id=id)
    if task.completed:
        task.completed = False
    else:
        task.completed = True
    task.save()
    return redirect('/')