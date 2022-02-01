from pydoc import describe
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
            return HttpResponseRedirect('/lists')
    else:
        form = TaskListForm()
    return render(request, 'tasks/create_task_list.html', {'form': form})


def create_pomodoro_task(request):
    my_lists = ((task_list.id, task_list.name) for task_list in TaskList.objects.all())
    if request.method == 'POST':
        form = TaskForm(request.POST, choices=my_lists)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            task_list = TaskList.objects.get(id=cleaned_data['task_list'])
            new_task = Task(name=cleaned_data['name'], completed=cleaned_data['completed'], 
                            target_date=cleaned_data['target_date'], task_list=task_list,
                            description=cleaned_data['description'])
            new_task.save()
            return HttpResponseRedirect('/lists')
    else:
        form = TaskForm(choices=my_lists)
    return render(request, 'tasks/create_task.html', {'form': form})


def edit_list(request, list_id):
    if request.method == 'POST':
        pass
    list = Task.objects.filter(task_list = list_id)
    # TODO
    # widok tasków z możliwością edycji
    return render(request, 'tasks/list_view.html', {'tasks_list': list})