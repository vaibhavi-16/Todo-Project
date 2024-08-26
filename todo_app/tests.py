from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Todo

class TodoTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.todo_data = {'title': 'Test Todo', 'description': 'Test Description'}
        self.response = self.client.post(reverse('todo-list-create'), self.todo_data, format="json")

    def test_create_todo(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_todos(self):
        response = self.client.get(reverse('todo-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo(self):
        todo = Todo.objects.get()
        new_data = {'title': 'Updated Todo', 'description': 'Updated Description'}
        response = self.client.put(reverse('todo-detail', kwargs={'pk': todo.id}), new_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo(self):
        todo = Todo.objects.get()
        response = self.client.delete(reverse('todo-detail', kwargs={'pk': todo.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
