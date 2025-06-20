from django.urls import path, include
from rest_framework.routers import DefaultRouter
from annonces.views import AnnonceVenteViewSet, PropositionAchatViewSet

router = DefaultRouter()
router.register(r'annonces-vente', AnnonceVenteViewSet, basename='annonces-vente')
router.register(r'propositions-achat', PropositionAchatViewSet, basename='propositions-achat')

urlpatterns = [
    path('', include(router.urls)),
]
