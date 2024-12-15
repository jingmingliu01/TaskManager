from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator


def task_list(request):
    query = request.GET.get('q', '') # get the search query from the request
    today = request.GET.get('today') # get the today query from the request
    tasks = Task.objects.all().order_by('start_time') # Query the Task model to get all tasks, ordered by start_time
    if today:
        now = timezone.now().date()  # get the current date
        tasks = tasks.filter(start_time__date__lte=now, end_time__date__gte=now)
    if query:
        tasks = tasks.filter(title__icontains=query) # filter the tasks by the search query
    paginator = Paginator(tasks, 5)  # every page shows 5 tasks
    page_number = request.GET.get('page')  # get the current page number
    page_obj = paginator.get_page(page_number)  # get the current page object
    return render(request, 'task_list.html',
                  {'tasks': page_obj, 'query': query})  # pass the page object to the template


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
