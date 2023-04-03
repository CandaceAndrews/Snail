 Django Rest Framework - SearchFilter

__________________________
from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']
__________________________



'author__name' is a lookup that specifies a related field in the search query. It is used to search for books based on the name of their associated author.

In the Book model, the author field is defined as a foreign key to the Author model:

__________________________
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
__________________________

Since author is a foreign key, you can use the double underscore (__) syntax to reference fields on the related Author model. In this case, 'author__name' specifies the name field on the Author model, which is used to search for books by the name of their associated author.

So when you use 'author__name' in search_fields, it tells Django Rest Framework to search for the search term in the name field of the related Author model when performing the search query on the Book model.