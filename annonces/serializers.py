from rest_framework import serializers
from .models import AnnonceVente, PropositionAchat, Commande, Candidature

class AnnonceVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnonceVente
        fields = '__all__'

class PropositionAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropositionAchat
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = '__all__'
