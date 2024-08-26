from django.urls import path
from .views import *

urlpatterns = [
    path('todos/', TodoListCreate.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailUpdateDelete.as_view(), name='todo-detail'),

]
