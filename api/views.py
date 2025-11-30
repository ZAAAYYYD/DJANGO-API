"""
Vues API pour le projet Concessionnaire.

Ce module contient toutes les APIViews pour gérer les concessionnaires,
les véhicules et les utilisateurs.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Concessionnaire, Vehicule
from .serializers import ConcessionnaireSerializer, VehiculeSerializer, UserSerializer


# ============================================================================
# Vues pour les Concessionnaires
# ============================================================================

class ConcessionnaireListView(APIView):
    """
    Vue pour lister tous les concessionnaires.
    
    GET /api/concessionnaires/
    Retourne la liste de tous les concessionnaires (sans le siret).
    """
    def get(self, request):
        concessionnaires = Concessionnaire.objects.all()
        serializer = ConcessionnaireSerializer(concessionnaires, many=True)
        return Response(serializer.data)


class ConcessionnaireDetailView(APIView):
    """
    Vue pour obtenir les détails d'un concessionnaire spécifique.
    
    GET /api/concessionnaires/<id>/
    Retourne les détails d'un concessionnaire (sans le siret).
    """
    def get(self, request, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=pk)
        serializer = ConcessionnaireSerializer(concessionnaire)
        return Response(serializer.data)


# ============================================================================
# Vues pour les Véhicules
# ============================================================================

class VehiculeListView(APIView):
    """
    Vue pour lister les véhicules d'un concessionnaire.
    
    GET /api/concessionnaires/<id>/vehicules/
    Retourne tous les véhicules liés à un concessionnaire spécifique.
    """
    def get(self, request, concessionnaire_pk):
        # Vérifie que le concessionnaire existe
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
        # Récupère tous les véhicules de ce concessionnaire
        vehicules = Vehicule.objects.filter(concessionnaire=concessionnaire)
        serializer = VehiculeSerializer(vehicules, many=True)
        return Response(serializer.data)


class VehiculeDetailView(APIView):
    """
    Vue pour obtenir les détails d'un véhicule spécifique.
    
    GET /api/concessionnaires/<id>/vehicules/<id>/
    Retourne les détails d'un véhicule appartenant à un concessionnaire.
    """
    def get(self, request, concessionnaire_pk, pk):
        # Vérifie que le concessionnaire existe
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
        # Récupère le véhicule spécifique de ce concessionnaire
        vehicule = get_object_or_404(
            Vehicule, 
            pk=pk, 
            concessionnaire=concessionnaire
        )
        serializer = VehiculeSerializer(vehicule)
        return Response(serializer.data)


# ============================================================================
# Vues Bonus - Authentification
# ============================================================================

class UserCreateView(APIView):
    """
    Vue pour créer un nouvel utilisateur (endpoint bonus).
    
    POST /api/users/
    Crée un nouvel utilisateur avec username, email et password.
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

