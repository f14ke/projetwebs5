"""projectwebs5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
   https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
   1. Add an import:  from my_app import views
   2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
   1. Add an import:  from other_app.views import Home
   2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
   1. Import the include() function: from django.urls import include, path
   2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


# Views dont on créé les urlpatterns.
from GestionEDT.views import *

# Bootstrap Crud Template
from bsct.urls import URLGenerator

""" Génération automatique de toutes les URLs de création, détails, etc.
   #'c' - Refers to the Create CRUD type
   #'r' - Refers to the Read/Detail CRUD type
   #'u' - Refers to the Update/Edit CRUD type
   #'d' - Refers to the Delete CRUD type
   #'l' - Refers to the List CRUD type
"""
bsct_patterns_p = URLGenerator( Professeur ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_e = URLGenerator( Etudiant ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_u = URLGenerator( UC ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_sa = URLGenerator( Salle ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_se = URLGenerator( Seance ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_g = URLGenerator( Groupe ).get_urlpatterns(crud_types = 'crudl')
bsct_patterns_f = URLGenerator( Formation ).get_urlpatterns(crud_types = 'crudl')

urlpatterns = [
   # Index
   path('', home, name = 'homepage'),
   path('index/', home, name = 'homepage'),
   path('home/', home, name = 'homepage'),
   path('etudiant_import/',import_fichier,name='etudiant_import'),
   path('etudiant_export/',export_etudiant_csv,name='etudiant_export'),

   url( '', include( bsct_patterns_p ) ),
   url( '', include( bsct_patterns_e ) ), 
   url( '', include( bsct_patterns_u ) ), 
   url( '', include( bsct_patterns_sa ) ), 
   url( '', include( bsct_patterns_se ) ), 
   url( '', include( bsct_patterns_g ) ), 
   url( '', include( bsct_patterns_f ) )
]
