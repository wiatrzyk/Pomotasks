from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

import json
from .forms import TaskForm, TaskListForm
from .models import TaskList, Task



def home_page(request):
    return render(request, 'tasks/base.html', {})

@login_required
def timer(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/timer.html', {'task': task})

@login_required
def edit_list(request, list_id):
    list = Task.objects.filter(task_list = list_id, user=request.user)
    p = Paginator(list, 3)
    return render(request, 'tasks/list_view.html', {'tasks_list': p})

@login_required
def tasks(request):
    all_tasks = TaskList.objects.filter(user=request.user)
    return render(request, 'tasks/tasks_list.html', {'task_list': all_tasks})

@login_required
def create_task_list(request):
    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_list = TaskList(name=name, user=request.user)
            new_list.save()
            return HttpResponseRedirect('/lists')
    else:
        form = TaskListForm()
    return render(request, 'tasks/create_task_list.html', {'form': form})

@login_required
def create_pomodoro_task(request):
    my_lists = ((task_list.id, task_list.name) for task_list in TaskList.objects.filter(user=request.user))
    if request.method == 'POST':
        form = TaskForm(request.POST, choices=my_lists)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            task_list = TaskList.objects.get(id=cleaned_data['task_list'], user=request.user)
            new_task = Task(name=cleaned_data['name'], completed=cleaned_data['completed'], 
                            target_date=cleaned_data['target_date'], task_list=task_list,
                            description=cleaned_data['description'], user=request.user)
            new_task.save()
            return HttpResponseRedirect('/lists')
    else:
        form = TaskForm(choices=my_lists)
    return render(request, 'tasks/create_task.html', {'form': form})


@login_required
def update_task(request, task_id):
    my_lists = ((task_list.id, task_list.name) for task_list in TaskList.objects.all())
    if request.method == 'POST':
        form = TaskForm(request.POST, choices=my_lists)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            task_list = TaskList.objects.get(id=cleaned_data['task_list'], user=request.user)
            task = Task.objects.get(id=task_id, user=request.user)
            task.name = cleaned_data['name']
            task.completed = cleaned_data['completed']
            task.target_date = cleaned_data['target_date']
            task.description = cleaned_data['description']
            task.task_list = task_list
            task.save()
            return HttpResponseRedirect('/lists')
    else:
        original_task = Task.objects.get(id=task_id, user=request.user)
        original_values = {
            'name': original_task.name,
            'task_list': original_task.task_list_id,
            'description': original_task.description,
            'completed': original_task.completed,
            'target_date': original_task.target_date,
        }
        form = TaskForm(initial = original_values, choices=my_lists)
    return render(request, 'tasks/update_task.html', {'form': form, 'task_id': task_id})

@login_required
def update_time(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            task = Task.objects.get(id=body['task_id'], user=request.user)
            task.pomodoros += 1
            task.save(update_fields=['pomodoros'])
        except:
            return HttpResponseBadRequest()
        return HttpResponse(200)
    else:
        return HttpResponseNotFound()