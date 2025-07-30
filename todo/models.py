from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    CATEGORY_CHOICES = [
        ("free", "자유"),
        ("travel", "여행"),
        ("cat", "고양이"),
        ("dog", "강아지"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="free")
    title = models.CharField(max_length=100)
    description = models.TextField("본문")
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title