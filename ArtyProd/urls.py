from django.urls import include, path

from . import views


urlpatterns = [	
    path('contact/', views.contact, name='contact'),
    path('service/', views.services, name='service'),
    path('equipe/', views.equipe, name='equipe'),
    path('personnel/<int:equipe_id>/', views.personnel, name='personnel'),
    path('', views.projet, name='projet'),
    path('add_projet/', views.add_projet, name='add_projet'),
    path('projet/<int:projet_id>/edit/', views.edit_projet, name='edit_projet'),
    path('projet/<int:projet_id>/delete/', views.delete_projet, name='delete_projet'),
     #-----------------------------SERVICE------------------------------------
    path('add_service/', views.add_service, name='add_service'),
    path('services/<int:service_id>/edit/', views.edit_service, name='edit_service'),
    path('services/<int:service_id>/delete/', views.delete_service, name='delete_service'),
    #--------------------------------EQUIPE-------------------------------------
    path('add_equipe/', views.add_equipe, name='add_equipe'),
    path('equipes/<int:equipe_id>/edit/', views.edit_equipe, name='edit_equipe'),
    path('equipes/<int:equipe_id>/delete/', views.delete_equipe, name='delete_equipe'),
        #--------------------------------PERSONNEL---------------------------------------
    path('personnel/<int:equipe_id>/', views.personnel, name='personnel'),
    path('personnel/add/', views.add_personnel, name='add_personnel'),
    path('personnel/<int:personnel_id>/edit/', views.edit_personnel, name='edit_personnel'),
    path('personnel/<int:personnel_id>/delete/', views.delete_personnel, name='delete_personnel'),
     #--------------------------------DEMANDE PROJET---------------------------------------
    path('demande_projet/', views.demande_projet, name='demande_projet'),
    path('demande_projet_list/', views.demande_projet_list, name='demande_projet_list'),
    path('demande_projet/<int:demande_projet_id>/edit/', views.modifier_demande_projet, name='modifier_demande_projet'),
    path('demande_projet/<int:demande_projet_id>/delete/', views.supprimer_demande_projet, name='supprimer_demande_projet'),
    
    

    ]