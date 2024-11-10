from rest_framework import viewsets
from .models import Book, Todo
from .serializers import BookSerializer, TodosSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodosSerializer