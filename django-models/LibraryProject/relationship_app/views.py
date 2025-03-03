from django.shortcuts import render  # ✅ For rendering templates
from django.views.generic.detail import DetailView  # ✅ For class-based views
from .models import Library, Book  # ✅ Fix: Import both models

# Function-Based View (FBV) for listing books
def list_books(request):
    books = Book.objects.all()  # ✅ Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ Pass books to template

# Class-Based View (CBV) for displaying a library's details
class LibraryDetailView(DetailView):
    model = Library  # ✅ Tell Django this is for Library data
    template_name = 'relationship_app/library_detail.html'  # ✅ Ensure this template exists
    context_object_name = 'library'  # ✅ In the template, access data as {{ library }}
