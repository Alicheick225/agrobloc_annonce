from rest_framework import serializers
from .models import AnnonceVente, PropositionAchat, Commande, Candidature

class AnnonceVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnonceVente
        fields = ['id', 'user_id', 'produit_id', 'prevision', 'statut', 'created_at', 'updated_at']

class PropositionAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropositionAchat
        fields = ['id', 'user_id', 'type_culture_id', 'quantite', 'statut', 'created_at', 'updated_at']

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ['id', 'annonce_vente_id', 'acheteur_id', 'quantite', 'statut', 'created_at', 'updated_at']

class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = ['id', 'proposition_achat_id', 'producteur_id', 'statut', 'created_at', 'updated_at']
