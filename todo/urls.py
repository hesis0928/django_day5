from django.urls import path
from . import views

app_name = 'todo'  # URL 이름공간 지정 (선택)

urlpatterns = [
    path('todo/',              views.todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', views.todo_info, name='todo_info'),
]
