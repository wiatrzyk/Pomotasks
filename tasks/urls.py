from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('lists/', views.tasks),
    path('create_task/', views.create_pomodoro_task),
    path('create_task_list/', views.create_task_list),
    path('lists/<list_id>', views.edit_list),

]
