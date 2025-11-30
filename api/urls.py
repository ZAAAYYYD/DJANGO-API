"""
Configuration des URLs pour l'application API.

Routes disponibles:
- GET /api/concessionnaires/ : Liste des concessionnaires
- GET /api/concessionnaires/<id>/ : Détails d'un concessionnaire
- GET /api/concessionnaires/<id>/vehicules/ : Liste des véhicules d'un concessionnaire
- GET /api/concessionnaires/<id>/vehicules/<id>/ : Détails d'un véhicule

Routes bonus (authentification JWT):
- POST /api/users/ : Création d'un utilisateur
- POST /api/token/ : Obtention d'un token JWT
- POST /api/refresh_token/ : Rafraîchissement du token JWT
"""
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    ConcessionnaireListView,
    ConcessionnaireDetailView,
    VehiculeListView,
    VehiculeDetailView,
    UserCreateView,
)

urlpatterns = [
    # Endpoints Concessionnaires
    path('concessionnaires/', ConcessionnaireListView.as_view(), name='concessionnaire-list'),
    path('concessionnaires/<int:pk>/', ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
    
    # Endpoints Véhicules (imbriqués sous concessionnaires)
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/', VehiculeListView.as_view(), name='vehicule-list'),
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/<int:pk>/', VehiculeDetailView.as_view(), name='vehicule-detail'),
    
    # Endpoints Bonus - Authentification JWT
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token-refresh'),
]

