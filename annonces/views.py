from rest_framework import generics, viewsets
from annonces.models import AnnonceVente, PropositionAchat

from annonces.serializers import AnnonceVenteSerializer, PropositionAchatSerializer
from .models import AnnonceVente, PropositionAchat, Commande, Candidature
from .serializers import (
    AnnonceVenteSerializer,
    PropositionAchatSerializer,
    CommandeSerializer,
    CandidatureSerializer,
)


# --- AnnonceVente ---

class AnnonceVenteList(generics.ListAPIView):
    queryset = AnnonceVente.objects.all()
    serializer_class = AnnonceVenteSerializer

class AnnonceVenteCreate(generics.CreateAPIView):
    queryset = AnnonceVente.objects.all()
    serializer_class = AnnonceVenteSerializer

class AnnonceVenteDetail(generics.RetrieveAPIView):
    queryset = AnnonceVente.objects.all()
    serializer_class = AnnonceVenteSerializer
    lookup_field = 'id'

class AnnonceVenteUpdate(generics.UpdateAPIView):
    queryset = AnnonceVente.objects.all()
    serializer_class = AnnonceVenteSerializer
    lookup_field = 'id'

class AnnonceVentePartialUpdate(generics.UpdateAPIView):
    queryset = AnnonceVente.objects.all()
    serializer_class = AnnonceVenteSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class AnnonceVenteDelete(generics.DestroyAPIView):
    queryset = AnnonceVente.objects.all()
    serializer_class = AnnonceVenteSerializer
    lookup_field = 'id'


# --- PropositionAchat ---

class PropositionAchatList(generics.ListAPIView):
    queryset = PropositionAchat.objects.all()
    serializer_class = PropositionAchatSerializer
    
class PropositionAchatCreate(generics.CreateAPIView):
    queryset = PropositionAchat.objects.all()
    serializer_class = PropositionAchatSerializer

class PropositionAchatDetail(generics.RetrieveAPIView):
    queryset = PropositionAchat.objects.all()
    serializer_class = PropositionAchatSerializer
    lookup_field = 'id'

class PropositionAchatUpdate(generics.UpdateAPIView):
    queryset = PropositionAchat.objects.all()
    serializer_class = PropositionAchatSerializer
    lookup_field = 'id'

class PropositionAchatPartialUpdate(generics.UpdateAPIView):
    queryset = PropositionAchat.objects.all()
    serializer_class = PropositionAchatSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class PropositionAchatDelete(generics.DestroyAPIView):
    queryset = PropositionAchat.objects.all()
    serializer_class = PropositionAchatSerializer
    lookup_field = 'id'


# --- Commande ---

class CommandeList(generics.ListAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

class CommandeCreate(generics.CreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

class CommandeDetail(generics.RetrieveAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    lookup_field = 'id'

class CommandeUpdate(generics.UpdateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    lookup_field = 'id'

class CommandePartialUpdate(generics.UpdateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class CommandeDelete(generics.DestroyAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    lookup_field = 'id'


# --- Candidature ---

class CandidatureList(generics.ListAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer

class CandidatureCreate(generics.CreateAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer

class CandidatureDetail(generics.RetrieveAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    lookup_field = 'id'

class CandidatureUpdate(generics.UpdateAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    lookup_field = 'id'

class CandidaturePartialUpdate(generics.UpdateAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class CandidatureDelete(generics.DestroyAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    lookup_field = 'id'
