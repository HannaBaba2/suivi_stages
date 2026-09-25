from django.db import models


class Entreprise(models.Model):

    SECTEUR_CHOICES = [
        ("informatique", "Informatique"),
        ("banque", "Banque"),
        ("sante", "Santé"),
        ("autre", "Autre"),
    ]

    nom = models.CharField(max_length=150, unique=True)
    ville = models.CharField(max_length=100)
    secteur = models.CharField(max_length=20, choices=SECTEUR_CHOICES)
    email = models.EmailField()

    def __set__(self):
        return f"{self.nom}({self.ville})"

