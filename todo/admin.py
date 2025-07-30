from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        'user_username',
        'title',
        'category',
        'is_completed',
        'created_at',
    )
    list_editable = ('is_completed',)

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = '작성자'
    user_username.admin_order_field = 'user__username'
