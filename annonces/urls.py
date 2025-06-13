from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnnonceVenteViewSet, PropositionAchatViewSet, CommandeViewSet, CandidatureViewSet

router = DefaultRouter()
router.register('ventes', AnnonceVenteViewSet)
router.register('achats', PropositionAchatViewSet)
router.register('commandes', CommandeViewSet)
router.register('candidatures', CandidatureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]