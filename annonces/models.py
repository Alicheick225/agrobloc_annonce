from django.db import models
from django.contrib.auth.models import User

from django.db import models

class AnnonceVente(models.Model):
    id = models.AutoField(primary_key=True)
    produit_id = models.IntegerField()
    prevision = models.BooleanField(default=False)
    statut = models.CharField(max_length=50, default='en attente')
    user_id = models.IntegerField()

    def __str__(self):
        return f"AnnonceVente #{self.id} - Produit {self.produit_id}"

    class Meta:
        managed = False
        db_table = 'annonce_vente'


class PropositionAchat(models.Model):
    id = models.AutoField(primary_key=True)
    type_culture_id = models.IntegerField()
    quantite = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.IntegerField()
    statut = models.CharField(max_length=50, default='en attente')

    def __str__(self):
        return f"PropositionAchat #{self.id} - Culture {self.type_culture_id}"

    class Meta:
        managed = False
        db_table = 'proposition_achat'


class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    annonce_vente_id = models.IntegerField()  # Clé étrangère mais conservée comme IntegerField vu ta logique actuelle
    statut = models.CharField(max_length=50, default='en attente')
    acheteur_id = models.IntegerField()
    quantite = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Commande #{self.id} - Vente {self.annonce_vente_id} - Acheteur {self.acheteur_id}"

    class Meta:
        managed = False
        db_table = 'commande'


class Candidature(models.Model):
    id = models.AutoField(primary_key=True)
    proposition_achat_id = models.IntegerField()  # Clé étrangère mais IntegerField pour coller à ta logique
    statut = models.CharField(max_length=50, default='en attente')
    date = models.DateTimeField(auto_now_add=True)
    producteur_id = models.IntegerField()

    def __str__(self):
        return f"Candidature #{self.id} - Proposition {self.proposition_achat_id}"

    class Meta:
        managed = False
        db_table = 'candidature'
