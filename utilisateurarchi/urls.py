from django.urls import path

from . import views

urlpatterns = [
    path('', views.inscription, name="inscription"),
    # path('connexion', views.connexion, name="connexion"),
    # path('deconnexion', views.deconnexion, name="deconnexion"),


]