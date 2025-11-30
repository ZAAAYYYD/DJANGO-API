"""
Modèles de données pour l'API Concessionnaire.
"""
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Concessionnaire(models.Model):
    """
    Modèle représentant un concessionnaire automobile/moto.
    
    Attributs:
        nom: Nom du concessionnaire (max 64 caractères)
        siret: Numéro SIRET (exactement 14 caractères, obligatoire)
    """
    nom = models.CharField(
        max_length=64,
        verbose_name="Nom du concessionnaire"
    )
    siret = models.CharField(
        max_length=14,
        validators=[
            MinLengthValidator(14, message="Le SIRET doit contenir exactement 14 caractères."),
            MaxLengthValidator(14, message="Le SIRET doit contenir exactement 14 caractères.")
        ],
        verbose_name="Numéro SIRET"
    )

    class Meta:
        verbose_name = "Concessionnaire"
        verbose_name_plural = "Concessionnaires"

    def __str__(self):
        return self.nom


class Vehicule(models.Model):
    """
    Modèle représentant un véhicule (auto ou moto).
    
    Attributs:
        type: Type de véhicule (moto ou auto)
        marque: Marque du véhicule (max 64 caractères)
        chevaux: Puissance en chevaux
        prix_ht: Prix hors taxes
        concessionnaire: Relation vers le concessionnaire propriétaire
    """
    TYPE_CHOICES = [
        ('moto', 'Moto'),
        ('auto', 'Auto'),
    ]

    type = models.CharField(
        max_length=4,
        choices=TYPE_CHOICES,
        verbose_name="Type de véhicule"
    )
    marque = models.CharField(
        max_length=64,
        verbose_name="Marque"
    )
    chevaux = models.IntegerField(
        verbose_name="Puissance (chevaux)"
    )
    prix_ht = models.FloatField(
        verbose_name="Prix HT"
    )
    concessionnaire = models.ForeignKey(
        Concessionnaire,
        on_delete=models.CASCADE,
        related_name='vehicules',
        verbose_name="Concessionnaire"
    )

    class Meta:
        verbose_name = "Véhicule"
        verbose_name_plural = "Véhicules"

    def __str__(self):
        return f"{self.marque} ({self.type}) - {self.prix_ht}€ HT"

