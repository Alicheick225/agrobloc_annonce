from django.contrib import admin
from .models import AnnonceVente

@admin.register(AnnonceVente)
class AnnonceVenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type_culture_id', 'parcelle_id', 'prevision', 'statut', 'quantite', 'prix_kg')
