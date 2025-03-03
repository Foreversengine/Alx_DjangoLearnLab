from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include('relationship_app.urls')),  # This connects your app’s URLs to the root
]