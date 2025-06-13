from rest_framework import viewsets
from .models import AnnonceVente, PropositionAchat, Commande, Candidature
from .serializers import (
    AnnonceVenteSerializer, PropositionAchatSerializer,
    CommandeSerializer, CandidatureSerializer
)

class AnnonceVenteViewSet(viewsets.ModelViewSet):
    queryset = AnnonceVente.objects.all()
    serializer_class = AnnonceVenteSerializer

class PropositionAchatViewSet(viewsets.ModelViewSet):
    queryset = PropositionAchat.objects.all()
    serializer_class = PropositionAchatSerializer

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

class CandidatureViewSet(viewsets.ModelViewSet):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
