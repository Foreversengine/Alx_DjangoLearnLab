from django.urls import path
from . import views

urlpatterns = [
    path('author/<str:author_name>/', views.author_books, name='author_books'),
    path('library/<str:library_name>/', views.library_books, name='library_books'),
    path('librarian/<str:library_name>/', views.librarian_details, name='librarian_details'),
]