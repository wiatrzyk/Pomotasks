from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('lists/', views.tasks),
    path('task/<task_id>', views.timer, name="timer"),
    path('create_task/', views.create_pomodoro_task),
    path('create_task_list/', views.create_task_list),
    path('lists/<list_id>', views.edit_list),
    path('update_task/<task_id>', views.update_task),
    path('update_time/', views.update_time, name="update_task_time"),
]
