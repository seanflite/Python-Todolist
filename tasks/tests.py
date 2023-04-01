from rest_framework import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from .models import TodoItem, TodoList


class TodoListViewSetTests(APITestCase):
    url = '/api/todo_lists/'
    def setUp(self):
        TodoList.objects.create(title = "unitTest1")

    def test_list_todoList(self):
        response = self.client.get(self.url)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result[0]['title'], 'unitTest1')
    
    def test_post_todoList(self):
        data = {
            'title': 'unitTest2'
        }
        
        response = self.client.post(self.url, data)
        result = response.json()
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['title'], data['title'])
        
    def test_update_todoList(self):
        data_original = {
            "title": "unitTestOriginal"
        }
        responseBeforeUpdate = self.client.post(self.url, data_original)
        resultBeforeUpdate = responseBeforeUpdate.data
        todoListId = resultBeforeUpdate['id']
        data_updated = {
            "title": "unitTestUpdated"
        }
        response = self.client.put(self.url + f'{todoListId}/', data_updated)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['title'], data_updated['title'])
    
    def test_delete_todoList(self):
        data_original = {
            "title": "unitTestOriginal"
        }
        response = self.client.post(self.url, data_original)
        result = response.data
        todoListId = result['id']
        response_del = self.client.delete(self.url + f"{todoListId}/")
        response_get = self.client.get(self.url + f"{todoListId}/")
        
        self.assertEqual(response_del.status_code, 204)
        self.assertEqual(response_get.status_code, 404)
        
class TodoItemsViewSetTests(APITestCase):
    url = '/api/todo_items/'
    url_todoList = '/api/todo_lists/'
    
    def setUp(self):
        todoList = TodoList.objects.create(title = "unitTest1")
        todoItem = TodoItem.objects.create(title="unitTest_todoItem1", todo_list=todoList, completed=False)
        
    def test_list_todoItems(self):
        response = self.client.get(self.url)
        result = response.data
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result[0]['title'], "unitTest_todoItem1")
    
    def test_post_todoItems(self):
        todoList = TodoList.objects.create(title = "unitTest1")
        data = {
            'title': 'unitTest_todoItem2',
            'todo_list' : todoList.id,
            'completed' : 'false'
        }
        response = self.client.post(self.url, data)
        result = response.json()
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['title'], data['title'])
        
    def test_update_todoItems(self):
        todoList = TodoList.objects.create(title = "unitTest1")
        todoItem = TodoItem.objects.create(title="unitTest_todoItem3", todo_list=todoList, completed=False)
        
        data = {
            'title': 'unitTest_todoItem_updated',
            'todo_list' : todoList.id,
            'completed' : 'false'
        }
        response = self.client.put(self.url + f'{todoItem.id}/', data)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['title'], data['title'])
    
    def test_delete_todoItems_WHEN_TodoItems_Deleted_THEN_Deleted(self):
        todoList = TodoList.objects.create(title = "unitTest1")
        todoItem = TodoItem.objects.create(title="unitTest_todoItem4", todo_list=todoList, completed=False)
        
        response_del = self.client.delete(self.url + f"{todoItem.id}/")
        response_get = self.client.get(self.url + f"{todoItem.id}/")
        
        self.assertEqual(response_del.status_code, 204)
        self.assertEqual(response_get.status_code, 404)
    
    def test_delete_todoItems_WHEN_TodoList_Deleted_THEN_TodoItems_Deleted(self):
        todoList = TodoList.objects.create(title = "unitTest1")
        todoItem = TodoItem.objects.create(title="unitTest_todoItem4", todo_list=todoList, completed=False)
        
        response_del_todoList = self.client.delete(self.url_todoList + f"{todoItem.id}/")
        response_get_todoItems = self.client.get(self.url + f"{todoItem.id}/")
        
        self.assertEqual(response_del_todoList.status_code, 204)
        self.assertEqual(response_get_todoItems.status_code, 404)