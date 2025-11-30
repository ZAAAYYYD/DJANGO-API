"""
Configuration de l'interface d'administration Django.
"""
from django.contrib import admin
from .models import Concessionnaire, Vehicule


@admin.register(Concessionnaire)
class ConcessionnaireAdmin(admin.ModelAdmin):
    """Administration pour les Concessionnaires."""
    list_display = ('id', 'nom', 'siret')
    search_fields = ('nom', 'siret')


@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    """Administration pour les Véhicules."""
    list_display = ('id', 'type', 'marque', 'chevaux', 'prix_ht', 'concessionnaire')
    list_filter = ('type', 'concessionnaire')
    search_fields = ('marque',)

