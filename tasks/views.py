from django.http import response, HttpResponseRedirect
from django.shortcuts import render

from .forms import TaskForm, TaskListForm
from .models import TaskList, Task


# Create your views here.
def home_page(request):
    return render(request, 'tasks/base.html', {})


def tasks(request):
    all_tasks = TaskList.objects.all()
    return render(request, 'tasks/tasks_list.html', {'task_list': all_tasks})


def create_task_list(request):
    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_list = TaskList(name=name)
            new_list.save()
            return HttpResponseRedirect('/tasks')
    else:
        form = TaskListForm()
    return render(request, 'tasks/create_task_list.html', {'form': form})


def create_pomodoro_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            name = cleaned_data['name']
            new_task = Task(name=name, completed=cleaned_data['completed'], target_date=cleaned_data['target_date'])
            new_task.save()
            return HttpResponseRedirect('/tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


def edit_list(request, list_id):
    if request.method == 'POST':
        pass
    list_name = TaskList.objects.get(id = list_id).name
    # TODO
    # widok tasków z możliwością edycji
    tasks = None
    return render(request, 'tasks/list_view.html', {'list_name': list_name, 'tasks':tasks})