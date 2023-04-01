from django.contrib import admin
from .models import TodoList, TodoItem

# Register your models here.
admin.site.register(TodoItem)

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_tags']
    
    
    def get_tags(self, obj):
        return ','.join(o for o in obj.tags.names())
