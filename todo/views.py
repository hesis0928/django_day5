from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Todo
from .forms import TodoForm, TodoUpdateForm

@login_required
def todo_list(request):
    q = request.GET.get('q', '')
    todos = Todo.objects.filter(user=request.user)
    if q:
        todos = todos.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q)
        )
    paginator = Paginator(todos.order_by('-created_at'), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'todo/todo_list.html', {'page_obj': page_obj, 'q': q})

@login_required
def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    return render(request, 'todo/todo_info.html', todo.__dict__)

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo:todo_info', todo_id=todo.id)
    else:
        form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form': form})

@login_required
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_info', todo_id=todo.id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'todo/todo_update.html', {'form': form, 'todo': todo})

@login_required
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('todo:todo_list')