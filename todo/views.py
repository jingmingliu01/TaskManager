from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator

def task_list(request):
    tasks = Task.objects.all()  # Query the Task model to get all tasks
    paginator = Paginator(tasks, 5)  # every page shows 10 tasks
    page_number = request.GET.get('page')  # get the current page number
    page_obj = paginator.get_page(page_number)  # get the current page object
    return render(request, 'task_list.html', {'tasks': page_obj})  # pass the page object to the template

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')