from django.contrib import admin
from .models import Client, DemandeProjet,Service,Projet,Equipe,Personnel

# Register your models here.
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Projet)
admin.site.register(Equipe)
admin.site.register(Personnel)
admin.site.register(DemandeProjet)

