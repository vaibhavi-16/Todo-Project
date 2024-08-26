import time
from celery import shared_task
from .models import Todo

@shared_task
def process_todo_data(todo_id):
    try:
        # Retrieve the Todo object
        todo = Todo.objects.get(id=todo_id)

        # Simulate some processing time (e.g., 5 seconds)
        time.sleep(5)

        # Update the Todo as completed
        todo.completed = True
        todo.save()

        # Return a success message
        return f"Successfully processed Todo with id: {todo_id}, marked as completed."

    except Todo.DoesNotExist:
        # Return a failure message if the Todo does not exist
        return f"Todo with id: {todo_id} does not exist."
