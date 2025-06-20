from django.contrib import admin
from .models import AnnonceVente, PropositionAchat, Commande, Candidature

@admin.register(AnnonceVente)
class AnnonceVenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'type_culture', 'parcelle', 'statut', 'quantite', 'prix_kg', 'created_at')
    list_filter = ('statut', 'prevision', 'created_at')
    search_fields = ('id', 'statut', 'user_id')

@admin.register(PropositionAchat)
class PropositionAchatAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_culture_id', 'user_id', 'statut', 'quantite')
    list_filter = ('statut',)
    search_fields = ('id',)

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'annonce_vente_id', 'acheteur_id', 'statut', 'quantite')
    list_filter = ('statut',)
    search_fields = ('id',)

@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'proposition_achat_id', 'producteur_id', 'statut', 'date')
    list_filter = ('statut', 'date')
    search_fields = ('id',)
