from django.shortcuts import render
from relationship_app.models import Author, Book, Library, Librarian

def author_books(request, author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return render(request, 'author_books.html', {'author': author, 'books': books})