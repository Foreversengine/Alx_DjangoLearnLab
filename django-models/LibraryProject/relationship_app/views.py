from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# User Registration View
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            return redirect('home')  # Redirect to home page (or change to a relevant page)
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User Login View
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View
def logout_user(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

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
