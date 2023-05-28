from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.user.username
    @receiver(post_save, sender=User)
    def create_client(sender, instance, created, **kwargs):
      if created:
          client = Client.objects.create(user=instance, address="", phone_number="")
          print(f"Created client {client.pk} for user {instance.username}")


class Service(models.Model):
    TYPE_CHOICES = [
        ('Design Graphique', 'Design Graphique'),
        ('Design Web', 'Design Web'),
        ('SC', 'Scénarisation'),
    ]
    
    nom = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ImageField( null=True, blank=True)
   
    def __str__(self):
        return self.nom


class Projet(models.Model):
    libelle = models.CharField(max_length=50)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve = models.BooleanField(default=False)
    image= models.ImageField(upload_to='media/', blank=True)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, null=True, blank=True)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    

    def __str__(self):
        return self.libelle
    
class Equipe(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image= models.ImageField( blank=True)
   
    
    def __str__(self):
        return self.nom
 
    


class Personnel(models.Model):
    nom = models.CharField(max_length=50)
    cv = models.TextField()
    photo = models.ImageField(upload_to='media/', blank=True)
    lien_fb = models.URLField(null=True, blank=True)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom   


class DemandeProjet(models.Model):
    libelle = models.CharField(max_length=50)
    description = models.TextField()
    date_demande = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    STATUT_CHOICES = [
        ('En attente', 'En attente'),
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé')
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES,default="En Attente")
    
    def __str__(self):
        return self.libelle   
class Detail(models.Model):
   fichier=models.FileField(upload_to="media/",max_length=250,null=True,default=None)
   service=models.ForeignKey(Service,on_delete=models.CASCADE,null=True)
   projet=models.ForeignKey(Projet,on_delete=models.CASCADE,null=True)
