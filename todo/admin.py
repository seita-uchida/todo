from django.contrib import admin
from .models import Task 

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "status", "due_date", "execution_date", "order", "created_at")
    list_filter = ("type", "status")
    search_fields = ("title",)
    ordering = ("order", "-created_at")