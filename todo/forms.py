from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['category', 'title', 'description', 'start_date', 'end_date']

class TodoUpdateForm(TodoForm):
    class Meta(TodoForm.Meta):
        fields = TodoForm.Meta.fields + ['is_completed']