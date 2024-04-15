from django.db import models

class Personne (models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=100)
 
class Voiture (models.Model):
    immatriculation=models.CharField(max_length=8, primary_key=True)
    mark=models.CharField(max_length=255, null=False)
    owner=models.ForeignKey(Personne, on_delete=models.CASCADE, null=False)
    image=models.CharField(max_length=255, null=False)
    

    
