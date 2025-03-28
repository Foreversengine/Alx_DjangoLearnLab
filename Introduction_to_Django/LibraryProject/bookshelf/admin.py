from django.contrib import admin
from .models import Book

# Custom Admin Class for the Book Model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for these fields
    list_filter = ('author', 'publication_year')

    # Enable search for these fields
    search_fields = ('title', 'author')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)