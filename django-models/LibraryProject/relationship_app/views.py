from django.shortcuts import render
from relationship_app.models import Author, Book, Library, Librarian

def author_books(request, author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return render(request, 'author_books.html', {'author': author, 'books': books})

def library_books(request, library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return render(request, 'library_books.html', {'library': library, 'books': books})

def librarian_details(request, library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return render(request, 'librarian_details.html', {'library': library, 'librarian': librarian})