from django.db import models


class ReservationsSeance(models.Model):
    nom = models.CharField(max_length=250)
    mail = models.EmailField(max_length=200, blank=True, null=True)
    Jour = models.DateTimeField(blank=True, null=True)
    HeureDebut = models.TimeField(blank=True, null=True)
    HeureFin = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.nom