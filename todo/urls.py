from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('<int:todo_id>/', views.todo_info, name='todo_info'),
    path('<int:todo_id>/update/', views.todo_update, name='todo_update'),
    path('<int:todo_id>/delete/', views.todo_delete, name='todo_delete'),
]