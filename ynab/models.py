

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class User(models.Model):
    nom = models.CharField(max_length=20)
    mot_de_passe = models.CharField(max_length=20)

class Categorie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    def type_categorie(self):
     def __str__(self):
         return self.type

class Depense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    montant = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    payment_method = models.CharField(max_length=50)

    def type_categorie(self):
       return self.categorie.type

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    montant = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    def type_categorie(self):
       return self.categorie.type
       
  

