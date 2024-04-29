from django.contrib import admin
from todo_list.models import ToDoItem


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'done', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    list_filter = ('done', 'created_at', 'updated_at')
