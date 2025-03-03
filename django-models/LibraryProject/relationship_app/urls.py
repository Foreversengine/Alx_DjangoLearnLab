from django.urls import path
from .views import list_books, LibraryDetailView  # Import your views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # List all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Library details
]