from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from annonces.models import AnnonceVente, PropositionAchat
from annonces.serializers import AnnonceVenteSerializer, PropositionAchatSerializer

class AnnonceVenteViewSet(viewsets.ModelViewSet):
    queryset = AnnonceVente.objects.all()
    serializer_class = AnnonceVenteSerializer
    #permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='mes-previsions')
    def previsions_utilisateur(self, request):
        user_id = request.user.id
        annonces = self.get_queryset().filter(user_id=user_id, prevision=True)
        serializer = self.get_serializer(annonces, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='mes-ventes')
    def ventes_directes_utilisateur(self, request):
        user_id = request.user.id
        annonces = self.get_queryset().filter(user_id=user_id, prevision=False)
        serializer = self.get_serializer(annonces, many=True)
        return Response(serializer.data)

class PropositionAchatViewSet(viewsets.ModelViewSet):
    queryset = PropositionAchat.objects.all()
    serializer_class = PropositionAchatSerializer
    #permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def propositions_utilisateur(self, request):
        user_id = request.user.id
        propositions = self.get_queryset().filter(user_id=user_id)
        serializer = self.get_serializer(propositions, many=True)
        return Response(serializer.data)
