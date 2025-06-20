from django.db import models
import uuid

class AnnonceVente(models.Model):
    import uuid
from django.db import models

class AnnonceVente(models.Model):
    STATUT_CHOICES = [
        ('prévision', 'Prévision'),
        ('a vendre', 'À vendre'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    type_culture = models.ForeignKey('types_culture.TypeCulture', on_delete=models.CASCADE)
    parcelle = models.ForeignKey('parcelles.Parcelle', on_delete=models.CASCADE)
    photo = models.CharField(max_length=255, blank=True, null=True)
    prevision = models.BooleanField(default=False)
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES)
    quantite = models.PositiveIntegerField()
    prix_kg = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"AnnonceVente #{self.id} - {self.statut} - {self.quantite} kg @ {self.prix_kg} €/kg"

    class Meta:
        managed = False  # Garde False si la table existe déjà
        db_table = 'annonces_vente'



class PropositionAchat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_culture_id = models.UUIDField()
    quantite = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.UUIDField()
    statut = models.CharField(max_length=50, default='en attente')

    def __str__(self):
        return f"PropositionAchat #{self.id} - Culture {self.type_culture_id}"

    class Meta:
        managed = False
        db_table = 'proposition_achat'


class Commande(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    annonce_vente_id = models.UUIDField()
    statut = models.CharField(max_length=50, default='en attente')
    acheteur_id = models.UUIDField()
    quantite = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Commande #{self.id} - Vente {self.annonce_vente_id} - Acheteur {self.acheteur_id}"

    class Meta:
        managed = False
        db_table = 'commandes'


class Candidature(models.Model):
    id = models.AutoField(primary_key=True)
    proposition_achat_id = models.IntegerField()
    statut = models.CharField(max_length=50, default='en attente')
    date = models.DateTimeField(auto_now_add=True)
    producteur_id = models.IntegerField()

    def __str__(self):
        return f"Candidature #{self.id} - Proposition {self.proposition_achat_id}"

    class Meta:
        managed = False
        db_table = 'candidature'
 