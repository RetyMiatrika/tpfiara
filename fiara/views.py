from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import Personne
from .forms import PersonneForm, VoitureForm

def personne(request):
    if request.method == 'GET':
        form = PersonneForm()
        personnes = Personne.objects.all()
        context = {
            "form": form,
            "personnes": personnes
        }
        return render(request, 'personne.html', context)
    
        
    elif request.method == 'POST':
        data= PersonneForm(request.POST)
        if data.is_valid():
            last=data.cleaned_data.get('last_name')
            first=data.cleaned_data.get('first_name')
            age=data.cleaned_data.get('age')
            gender=data.cleaned_data.get('gender')
            personne= Personne.objects.create(last_name=last, first_name=first, age=age, gender=gender)
            personne.save()
            return HttpResponse("ajout reussi")
        return HttpResponse("Ajout échoué")
        
        

def voiture(request):
    
    contex={
        "form": VoitureForm()
    }
    return render(request, "voiture.html", contex)

def accueil(request):
    return render(request, 'accueil.html')



def voiture_add(request):
    v=Voiture.objects.create(immatriculation="123456789", mark="Toyota")
    v.save()
    return HttpResponse(v)

def delete_personne(request,id):
    Personne.objects.filter(id=id).first().delete()
    return redirect("personne")

    