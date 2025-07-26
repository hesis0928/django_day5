# todo/urls.py
from django.urls import path
from . import views

app_name = 'todo'                   # ← 네임스페이스 선언
urlpatterns = [
    # 목록 보기 (/todo/)
    path('', views.todo_list, name='todo_list'),
    # 상세 보기 (/todo/1/, 2, 3…)
    path('<int:todo_id>/', views.todo_info, name='todo_info'),
]
