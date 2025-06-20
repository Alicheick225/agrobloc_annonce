from django.contrib import admin
from .models import AnnonceVente, PropositionAchat, Commande, Candidature

@admin.register(AnnonceVente)
class AnnonceVenteAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user_id', 'type_culture_id', 'parcelle_id', 'photo',
        'statut', 'quantite', 'prix_kg', 'created_at'
    ]
    list_filter = ['statut', 'created_at']
    search_fields = ['user_id', 'type_culture_id', 'parcelle_id', 'statut']

@admin.register(PropositionAchat)
class PropositionAchatAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'type_culture_id', 'quantite', 'statut', 'created_at']
    list_filter = ['statut', 'created_at']
    search_fields = ['user_id', 'type_culture_id', 'statut']

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id', 'annonce_vente_id', 'user_id', 'statut', 'quantite', 'created_at']
    list_filter = ['statut', 'created_at']
    search_fields = ['annonce_vente_id', 'user_id', 'statut']

@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'proposition_achat_id', 'user_id', 'statut', 'created_at']
    list_filter = ['statut', 'created_at']
    search_fields = ['proposition_achat_id', 'user_id', 'statut']
