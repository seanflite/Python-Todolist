from rest_framework import viewsets

from . import models
from . import serializers
from .models import TodoList, TodoItem
from django.contrib.auth.models import User
from .serializers import TodoListSerializer, TodoItemSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status


class TodoListViewSet(viewsets.ModelViewSet):
    """The TodoList viewset provides standard CRUD actions on the TodoList model."""
    queryset = models.TodoList.objects.order_by("pk")
    serializer_class = serializers.TodoListSerializer
    
    def todo_lists(self, request):
        if request.method == 'GET':
            todoList = TodoList.objects.all()
            serializer = TodoListSerializer(todoList, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            todo_list_data = request.data
            serializer = TodoListSerializer(todo_list_data)
            if serializer.is_valid:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def todoList_details(self, request, todoList_id):  
        try:
            todoList = TodoList.objects.get(id = todoList_id)
        except TodoList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = TodoListSerializer(todoList)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = TodoListSerializer(todoList, data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        elif request.method == 'DELETE':
            todoList.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        

class TodoItemViewSet(viewsets.ModelViewSet):
    """The TodoItem viewset provides standard CRUD actions on the TodoItem model."""
    queryset = models.TodoItem.objects.order_by("pk")
    serializer_class = serializers.TodoItemSerializer
    
    def todo_items(self, request, todoList_id):
        try:
            todoList = TodoList.objects.get(id = todoList_id)
        except TodoList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        todoItems = todoList.todoItems.all()
        
        if request.method == 'GET':
            todoItems = TodoItem.objects.all()
            serializer = TodoItemSerializer(todoItems)
            return Response(serializer.data)
        if request.method == 'POST':
            todo_item_data = request.data
            serializer = TodoItemSerializer(todo_item_data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def todoItem_details(self, request, todoList_id, todoItem_id):
        try:
            todoList = TodoList.objects.get(id = todoList_id)
        except TodoList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            TodoItem = TodoItem.objects.get(pk = todoItem_id)
        except TodoItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = TodoItemSerializer(TodoItem)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = TodoItemSerializer(TodoItem, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        elif request.method == 'DELETE':
            TodoItem.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ModelViewSet):
    """The TodoItem viewset provides standard CRUD actions on the TodoItem model."""
    queryset = models.User.objects.order_by("pk")
    serializer_class = serializers.UserSerializer
    
    def user_list(self, request):
        if request.method == 'GET':
            user = User.objects.all()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        if request.method == 'POST':
            user_data = request.data
            serializer = UserSerializer(user_data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


