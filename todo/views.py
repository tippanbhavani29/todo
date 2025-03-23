from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from todo.models import Task
def add(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
def home(request):
    
    tasks = Task.objects.filter(Iscompleted=False)
    completed=Task.objects.filter(Iscompleted=True).order_by('-created_at')
    return render(request, 'home.html', {'tasks': tasks,'completed':completed})
def mark_completed(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.Iscompleted=True
    task.save()

    return redirect('home')
def mark_uncompleted(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.Iscompleted=False
    task.save()
    return redirect('home')
def deleted_completed(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')
def edit_task(request,pk):
    from django.shortcuts import get_object_or_404, render, redirect

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)   
    
    if request.method == 'POST':
         
        task_name = request.POST.get('task')   
        task.task = task_name
        task.save()   
        return redirect('home')   

    else:
        
        content = {
            'task': task
        }
        return render(request, 'edit.html', content)

def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')


    