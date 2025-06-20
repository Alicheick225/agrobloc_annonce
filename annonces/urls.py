from django.urls import path
from .views import (
    AnnonceVenteList, AnnonceVenteCreate, AnnonceVenteDetail, AnnonceVenteUpdate, AnnonceVentePartialUpdate, AnnonceVenteDelete,
    PropositionAchatList, PropositionAchatCreate, PropositionAchatDetail, PropositionAchatUpdate, PropositionAchatPartialUpdate, PropositionAchatDelete,
    CommandeList, CommandeCreate, CommandeDetail, CommandeUpdate, CommandePartialUpdate, CommandeDelete,
    CandidatureList, CandidatureCreate, CandidatureDetail, CandidatureUpdate, CandidaturePartialUpdate, CandidatureDelete,
)

# -- Fin routes Djessira --

# AnnonceVente

urlpatterns = [
path('annonces/', AnnonceVenteList.as_view(), name='annoncevente-list'),#lister 
path('annonces/create/', AnnonceVenteCreate.as_view(), name='annoncevente-create'),#creer  
path('annonces/<uuid:id>/', AnnonceVenteDetail.as_view(), name='annoncevente-detail'),#afficher une annonce specifique 
path('annonces/update/<uuid:id>/', AnnonceVenteUpdate.as_view(), name='annoncevente-update'),#modifier
path('annonces/delete/<uuid:id>/', AnnonceVenteDelete.as_view(), name='annoncevente-delete'),#supprimer

# Ajouter une API pour récupérer les annonces d'un utilisateur spécifique

# PropositionAchat
path('propositions/', PropositionAchatList.as_view(), name='propositionachat-list'),#lister 
path('propositions/create/', PropositionAchatCreate.as_view(), name='propositionachat-create'),#creer
path('propositions/<uuid:id>/', PropositionAchatDetail.as_view(), name='propositionachat-detail'),#afficher pour l'utilisateur specifique 
path('propositions/update/<uuid:id>/', PropositionAchatUpdate.as_view(), name='propositionachat-update'),#modifier
path('propositions/delete/<uuid:id>/', PropositionAchatDelete.as_view(), name='propositionachat-delete'),#supprimer


# Commande
path('commandes/', CommandeList.as_view(), name='commande-list'),#lister 
path('commandes/create/', CommandeCreate.as_view(), name='commande-create'),#creer
path('commandes/<uuid:id>/', CommandeDetail.as_view(), name='commande-detail'),#afficher pour l'utilisateur specifique 
path('commandes/update/<uuid:id>/', CommandeUpdate.as_view(), name='commande-update'),#modifier
path('commandes/delete/<uuid:id>/', CommandeDelete.as_view(), name='commande-delete'),#supprimer


# Candidature
path('candidatures/', CandidatureList.as_view(), name='candidature-list'),#lister 
path('candidatures/create/', CandidatureCreate.as_view(), name='candidature-create'),#creer
path('candidatures/<uuid:id>/', CandidatureDetail.as_view(), name='candidature-detail'),#afficher pour l'utilisateur specifique 
path('candidatures/update/<uuid:id>/', CandidatureUpdate.as_view(), name='candidature-update'),#modifier
path('candidatures/delete/<uuid:id>/', CandidatureDelete.as_view(), name='candidature-delete'),#supprimer
    
]



