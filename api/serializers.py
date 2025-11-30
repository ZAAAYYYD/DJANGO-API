"""
Serializers pour l'API Concessionnaire.

Les serializers convertissent les instances de modèles en représentations JSON
et valident les données entrantes.
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Concessionnaire, Vehicule


class ConcessionnaireSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Concessionnaire.
    
    Note: Le champ 'siret' est explicitement exclu de l'API
    (ni en lecture, ni en écriture) comme demandé dans les spécifications.
    """
    class Meta:
        model = Concessionnaire
        fields = ['id', 'nom']  # siret exclu volontairement


class VehiculeSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Véhicule.
    
    Inclut tous les champs du modèle sans exception.
    """
    class Meta:
        model = Vehicule
        fields = ['id', 'type', 'marque', 'chevaux', 'prix_ht', 'concessionnaire']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer pour la création d'utilisateurs (endpoint bonus).
    
    Le mot de passe est en write_only pour des raisons de sécurité.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        """
        Crée un nouvel utilisateur avec un mot de passe hashé.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

