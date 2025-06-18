import uuid
from django.db import models

class AnnonceVente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField()
    produit_id = models.UUIDField()
    prevision = models.BooleanField(default=False)
    statut = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"AnnonceVente #{self.id} - Produit {self.produit_id}"

    class Meta:
        managed = False
        db_table = 'annonces_vente'

class PropositionAchat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField()
    type_culture_id = models.UUIDField()
    quantite = models.IntegerField()
    statut = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PropositionAchat #{self.id} - Culture {self.type_culture_id}"

    class Meta:
        managed = False
        db_table = 'proposition_achat'

class Commande(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    annonce_vente_id = models.UUIDField()
    acheteur_id = models.UUIDField()
    quantite = models.IntegerField()
    statut = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Commande #{self.id} - Vente {self.annonce_vente_id} - Acheteur {self.acheteur_id}"

    class Meta:
        managed = False
        db_table = 'commandes'

class Candidature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proposition_achat_id = models.UUIDField()
    producteur_id = models.UUIDField()
    statut = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Candidature #{self.id} - Proposition {self.proposition_achat_id}"

    class Meta:
        managed = False
        db_table = 'candidatures'
