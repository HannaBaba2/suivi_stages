from django.shortcuts import render
from .models import Entreprise


def liste_entreprises(request):
    entreprises = Entreprise.objects.all()
    return render(request, "stages/liste_entreprises.html", {"entreprises": entreprises})