from django.contrib import admin
from django.urls import path, include
from filehandler import views  # Import your views here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filehandler/', include('filehandler.urls')),  # Include filehandler URLs
    path('', views.upload_file, name='home'),  # Route for the empty path (root URL)
]