from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # ✅ Import UserCreationForm

# User Registration View
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            return redirect('home')  # Redirect to home or another page
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
            return redirect('home')  # Redirect to home
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View
def logout_user(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout
