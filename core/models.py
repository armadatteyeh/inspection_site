from django.db import models

class Visite(models.Model):
    total = models.IntegerField(default=0)

    def __str__(self):
        return f"Visites: {self.total}"