from rest_framework import serializers
from .models import AnnonceVente, PropositionAchat, Commande, Candidature


class AnnonceVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnonceVente
        fields = '__all__'

    def validate(self, data):
        if data.get('prevision') and data.get('statut') != 'prévision':
            raise serializers.ValidationError({
                'statut': "Si 'prevision' est True, le statut doit être 'prévision'."
            })
        if 'quantite' in data and data['quantite'] is not None and data['quantite'] <= 0:
            raise serializers.ValidationError({
                'quantite': "La quantité doit être supérieure à 0."
            })
        if 'prix_kg' in data and data['prix_kg'] is not None and data['prix_kg'] < 0:
            raise serializers.ValidationError({
                'prix_kg': "Le prix par kg doit être supérieur ou égal à 0."
            })
        return data


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
