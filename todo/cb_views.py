from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.http import HttpRequest

from .models import Todo

class OwnerOrAdminMixin(UserPassesTestMixin, SingleObjectMixin):
    """
    Mixin to allow only object owners or admin users to access/modify the object.
    """
    # for IDE type hints
    request: HttpRequest

    def test_func(self):
        todo = self.get_object()
        user = self.request.user
        return user.is_staff or todo.user == user

class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        qs = Todo.objects.all() if self.request.user.is_staff else Todo.objects.filter(user=self.request.user)
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(title__icontains=q) | Q(description__icontains=q)
            )
        return qs.order_by('-created_at')

class TodoDetailView(LoginRequiredMixin, OwnerOrAdminMixin, DetailView):
    model = Todo
    template_name = 'todo/todo_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_object().__dict__)
        return context

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['category', 'title', 'description', 'start_date', 'end_date', 'is_completed']
    template_name = 'todo/todo_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cbv:cbv_todo_info', kwargs={'pk': self.object.pk})

class TodoUpdateView(LoginRequiredMixin, OwnerOrAdminMixin, UpdateView):
    model = Todo
    fields = ['category', 'title', 'description', 'start_date', 'end_date', 'is_completed']
    template_name = 'todo/todo_update.html'

    def get_success_url(self):
        return reverse('cbv:cbv_todo_info', kwargs={'pk': self.object.pk})

class TodoDeleteView(LoginRequiredMixin, OwnerOrAdminMixin, DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('cbv:cbv_todo_list')