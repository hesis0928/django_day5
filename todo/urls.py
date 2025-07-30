from django.urls import path, include
from users.views import signup
from .cb_views import (
    TodoListView, TodoDetailView,
    TodoCreateView, TodoUpdateView, TodoDeleteView
)
from django.urls import path
from .views import (
    TodoListView, TodoDetailView,
    TodoCreateView, TodoUpdateView, TodoDeleteView
)

app_name = 'todo'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('todo/',             TodoListView.as_view(),   name='cbv_todo_list'),
    path('todo/create/',      TodoCreateView.as_view(), name='cbv_todo_create'),
    path('todo/<int:pk>/',    TodoDetailView.as_view(), name='cbv_todo_info'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='cbv_todo_update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='cbv_todo_delete'),
    path('',          TodoListView.as_view(),   name='list'),
    path('create/',   TodoCreateView.as_view(), name='create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='delete'),
]
