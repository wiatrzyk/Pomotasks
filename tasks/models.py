from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_list")
    name = models.CharField(max_length=255, default='New List')
    
    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task")
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='New Task')
    description = models.CharField(max_length=255, default='New Task')
    completed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    target_date = models.DateTimeField(default=None, null=True)
    pomodoros = models.IntegerField(default=0, null=False)
    target_pomodoros = models.IntegerField(default=1, null=False)

    def __str__(self) -> str:
        return f'{self.name}; complete status {self.completed}; creation date {self.creation_date}'
