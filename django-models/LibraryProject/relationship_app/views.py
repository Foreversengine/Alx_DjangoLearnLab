from django.shortcuts import render
from .models import Book  # Import the Book model

def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'list_books.html', {'books': books})  # Pass books to the template
from django.views.generic import DetailView
from .models import Library  # Import the Library model

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Use the HTML template for display
    context_object_name = 'library'  # The variable name in the template
