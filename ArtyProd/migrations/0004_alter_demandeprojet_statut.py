# Generated by Django 4.2.1 on 2023-05-23 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0003_alter_personnel_photo_demandeprojet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandeprojet',
            name='statut',
            field=models.CharField(choices=[('En attente', 'En attente'), ('En cours', 'En cours'), ('Terminé', 'Terminé')], default='En Attente', max_length=20),
        ),
    ]
