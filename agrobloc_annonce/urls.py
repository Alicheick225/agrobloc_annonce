from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Routes de l'application annonces
    path('api/annonces/', include('annonces.urls')),
]
