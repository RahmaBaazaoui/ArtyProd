from pyexpat.errors import messages
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.views.decorators.http import require_POST


from ArtyProd.forms import  DemandeProjetEditForm, DemandeProjetForm, EquipForm, PersonnelForm, ProjetForm, ServiceForm
from .models import Client, DemandeProjet,  Equipe, Personnel, Projet, Service
from django.contrib.auth.decorators import login_required
#-----------------------------------------------CONTACT--------------------------------------------------------------------------
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject=request.POST['subject']
        message = request.POST['message']

        message_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        send_mail(
            'Contact Form Submission',
            message_body,
            settings.DEFAULT_FROM_EMAIL,
            ['mohamedbenmannaa0@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'ArtyProd/contact/contact.html', {'success': True})
    return render(request, 'ArtyProd/contact/contact.html')
#-----------------------------------------------SERVICES--------------------------------------------------------------------------

def services(request):
    services = Service.objects.all()
    return render(request, 'ArtyProd/service/services.html', {'services': services})

#-----------------------------------------------PORTFOLIO--------------------------------------------------------------------------
def projet(request):	
  list= Projet.objects.all()
  return render( request, 'ArtyProd/portfolio/portfolio.html',{'list':list} )

#------------------------------------------------EQUIPE--------------------------------------------------------------------------
@login_required
def personnel(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    personnels = Personnel.objects.filter(equipe=equipe)
    context = {
        'equipe': equipe,
        'personnels': personnels,
    }
    return render(request, 'ArtyProd/equipe/personnel.html', context)

def equipe(request):
    equipe= Equipe.objects.all()
    return render(request, 'ArtyProd/equipe/equipe.html', {'equipe': equipe})

@require_POST
def delete_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    projet.delete()
    return redirect('projet')

def edit_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('projet')
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'ArtyProd/portfolio/edit_projet.html', {'form': form})

def add_projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projet')
    else:
        form = ProjetForm()
    return render(request, 'ArtyProd/portfolio/add_projet.html', {'form': form})

#-------------------------------------------CRUD SERVICES------------------------------------------------
@require_POST
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    return redirect('service')

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'ArtyProd/service/edit_service.html', {'form': form})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service')
    else:
        form = ServiceForm()
    return render(request, 'ArtyProd/service/add_service.html', {'form': form})

#----------------------------------------------- CRUD EQUIPE ------------------------------------------------------------
@require_POST
def delete_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    equipe.delete()
    return redirect('equipe')

def edit_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    if request.method == 'POST':
        form = EquipForm(request.POST, request.FILES, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('service')
    else:
        form = EquipForm(instance=equipe)
    return render(request, 'ArtyProd/equipe/edit_equipe.html', {'form': form})

def add_equipe(request):
    if request.method == 'POST':
        form = EquipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = EquipForm()
    return render(request, 'ArtyProd/equipe/add_equipe.html', {'form': form})

#-------------------------------------------- CRUD PERSONNEL ----------------------------------------------------------------------

@require_POST
def delete_personnel(request, personnel_id):
    personnel = get_object_or_404(Personnel, id=personnel_id)
    personnel.delete()
    return redirect('equipe')

def edit_personnel(request, personnel_id):
    personnel = get_object_or_404(Personnel, id=personnel_id)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = PersonnelForm(instance=personnel)
    return render(request, 'ArtyProd/equipe/edit_personnel.html', {'form': form})
def add_personnel(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = PersonnelForm()
    return render(request, 'ArtyProd/equipe/add_personnel.html', {'form': form})
#--------------------------------------------------DEMANDE PROJETS------------------------------------------------------------------

@login_required
def demande_projet(request):
    if request.method == 'POST':
        form = DemandeProjetForm(request.POST, request.FILES)
        if form.is_valid():
            demande_projet = form.save(commit=False)
            if request.user.is_authenticated:
                client = Client.objects.get(user=request.user)
                demande_projet.client = client
                demande_projet.save()
                return redirect('projet')
    else:
        form = DemandeProjetForm()
    return render(request, 'ArtyProd/demandeprojet/demande_projet.html', {'form': form})

def demande_projet_list(request):
    demandes_projet = DemandeProjet.objects.all()
    return render(request, 'ArtyProd/demandeprojet/demande_projet_list.html', {'demandes_projet': demandes_projet})

#---------------------------------------------------CRUD DEMANDE PROJET-----------------------------------------------------------------
def modifier_demande_projet(request, demande_projet_id):
    demande_projet = get_object_or_404(DemandeProjet, id=demande_projet_id)
    if request.method == 'POST':
        form = DemandeProjetEditForm(request.POST, instance=demande_projet)
        if form.is_valid():
            form.save()
            return redirect('demande_projet_list')
    else:
        form = DemandeProjetEditForm(instance=demande_projet)
    return render(request, 'ArtyProd/demandeprojet/modifier_demande_projet.html', {'form': form})

def supprimer_demande_projet(request, demande_projet_id):
    demande_projet = get_object_or_404(DemandeProjet, id=demande_projet_id)
    demande_projet.delete()
    return redirect('demande_projet_list')