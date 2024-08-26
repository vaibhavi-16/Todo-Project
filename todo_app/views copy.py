from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .tasks import process_todo_data
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure that only authenticated users can access this view

    def get_queryset(self):
        # Only return todos for the currently authenticated user
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save the new Todo object and associate it with the current user
        todo = serializer.save(user=self.request.user)
        
        # Trigger the background task to process the todo asynchronously
        process_todo_data.delay(todo.id)


