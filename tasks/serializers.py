from rest_framework import serializers
from .models import TodoItem, TodoList
from django.contrib.auth.models import User



class TodoListSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source = "created_by.username") #override the content of "created_by" field
    class Meta:
        model = TodoList
        fields = ["id", "created_at", "title","created_by", "todo_items"]
        depth = 1
        
class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ["id", "title", "todo_list", "completed", "description"]
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "todo_lists"]
        depth = 1
    