from django import forms

from .models import Personne
from .models import Voiture

class PersonneForm(forms.ModelForm):
    class Meta:
        model=Personne
        fields=("last_name", "first_name", "age", "gender")
        

class VoitureForm(forms.ModelForm):
    class Meta:
        model=Voiture
        fields=("immatriculation", "mark","image","owner")