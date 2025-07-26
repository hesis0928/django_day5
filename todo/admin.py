from django.contrib import admin
from .models import Todo          # ← Todo 모델을 가져옵니다

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'start_date',
        'end_date',
        'is_completed',
        'created_at',
        'modified_at',
    )
    list_editable = ('is_completed',)
