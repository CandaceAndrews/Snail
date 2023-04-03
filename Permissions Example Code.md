### Permissions Example

You can use Django's built-in permission system to control access to your views and APIs.
Here's an example of how you can set permissions for adding, updating, and deleting books:

Adding a new book: You can allow any authenticated user to add a new book as long as it doesn't already exist in the library.
You can achieve this by defining a custom permission class that checks if the book already exists in the database.

```
from rest_framework import generics, filters, permissions
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import BasePermission


class CanAddBook(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            title = request.data.get('title')
            author_id = request.data.get('author')
            if Book.objects.filter(title=title, author_id=author_id).exists():
                return False
        return True
```

You can then use this permission class in your view by including it in the permission_classes attribute:

```
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CanAddBook]
```

In this example, we're also using IsAuthenticatedOrReadOnly permission to allow any authenticated user to add
