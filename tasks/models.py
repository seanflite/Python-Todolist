from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class TodoList(models.Model):
    """A todo list contains TodoItems."""
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='todo_lists', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=256)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

class TodoItem(models.Model):
    title = models.CharField(max_length=256)
    todo_list = models.ForeignKey(TodoList, related_name = "todo_items", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False) 
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title