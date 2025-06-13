from django.contrib import admin
from .models import AnnonceVente, PropositionAchat, Commande, Candidature

@admin.register(AnnonceVente)
class AnnonceVenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'produit_id', 'prevision', 'statut', 'user_id')

@admin.register(PropositionAchat)
class PropositionAchatAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_culture_id', 'quantite', 'user_id', 'statut')

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'annonce_vente_id', 'statut', 'acheteur_id','quantite')

@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'proposition_achat_id', 'statut', 'date', 'producteur_id')
