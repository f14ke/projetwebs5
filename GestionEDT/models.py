from django.db import models 
from django.urls import reverse

from django.db.models import Model, BooleanField, CharField, IntegerField, DateField, DateTimeField, DecimalField, ForeignKey, EmailField
#import psycopg2.extension
from bsct.models import BSCTModelMixin

level_uni = (('L1', ('L1')),('L2', ('L2')),('L3', ('L3')),('M1', ('M1')),('M2', ('M2')))
semestre_uni = (('S1', ('S1')),('S2', ('S2')),('S3', ('S3')),('S4', ('S4')),
('S5', ('S5')),('S6', ('S6')),('S7', ('S7')),('S8', ('S8')),('S9', ('S9')),('S10', ('S10')))
statut_prof_uni = (('Professeur des universités', ('Professeur des universités')),
('Maître de conférences', ('Maître de conférences')))



# Create your models here.
class Professeur(BSCTModelMixin, models.Model):
   # Classe de Professeur.
   # BSCTModelMixin permet de ne pas écrire les méthodes get_absolute_url, get_delete_url...
   # Doc :
   #* https://pypi.org/project/django-bootstrap-crud-templates/
   # Exemple :
   #* https://github.com/Alem/django-bootstrap-crud-templates/blob/master/demo/crud/models.py

   num_professeur  = models.AutoField(primary_key=True)
   prenom         = models.CharField(max_length=30)       
   nom            = models.CharField(max_length=30)  
   adresse_courriel = models.EmailField(max_length=60)
   date_naissance = models.DateField()
   statut         = models.CharField(max_length=30, choices=statut_prof_uni)
   experience     = models.IntegerField()

   # La redéfinition de __str__ permet de changer le titre de la page détail
   def __str__(self):
      return self.prenom + ' ' + self.nom
   
   # Fields qui seront récupérés par BSCT pour générer les fields.
   @classmethod
   def get_allowed_fields(cls):
      return ['prenom', 'nom', 'adresse_courriel', 'date_naissance', 'statut', 'experience']

class Etudiant(models.Model):
   num_etudiant = models.IntegerField(primary_key=True)
   prenom      = models.CharField(max_length=30)       
   nom         = models.CharField(max_length=30)  
   adresse_courriel = models.EmailField(max_length=60)
   date_naissance       = models.DateField()
   niveau   = models.CharField(max_length=2, choices=level_uni,default=None) 
   fk_groupe   = models.ForeignKey("Groupe",on_delete=models.CASCADE)
   def __str__(self):
    return self.prenom + ' ' + self.nom
   def get_absolute_url(self):
     return reverse("etudiant-detail", kwargs={"num_etudiant": self.num_etudiant})

class UC(models.Model): 
   id_uc         = models.IntegerField(primary_key=True)
   nom_matiere   = models.CharField(max_length=30,default=' ')
   ects         = models.IntegerField()
   type_uc         = models.CharField(max_length=15)
   semestre     = models.CharField(max_length=3, choices=semestre_uni)
   fk_formation = models.ForeignKey("Formation",on_delete=models.CASCADE) # clés multiples
   def __str__(self):
    return self.nom_matiere
   def get_absolute_url(self):
     return reverse("uc-detail", kwargs={"id_uc": self.id_uc})

class Salle(models.Model):
   id_salle   = models.IntegerField(primary_key=True)
   code      = models.CharField(max_length=100)
   batiment  = models.CharField(max_length=100)
   capacite  = models.IntegerField()
   nb_pc      = models.IntegerField()
   projecteur= models.IntegerField()
   tableaux  = models.IntegerField()
   def __str__(self):
      return self.code + self.batiment
   def get_absolute_url(self):
      return reverse('salle-detail', kwargs={"id_salle": self.id_salle})

class Seance(models.Model): 
   id_seance      = models.IntegerField(primary_key=True)
   timecode_debut = models.DateTimeField()
   timecode_fin   = models.DateTimeField()
   fk_professeur = models.ForeignKey(Professeur,on_delete=models.CASCADE)
   fk_groupe     = models.ForeignKey(Etudiant,on_delete=models.CASCADE)
   fk_uc         = models.ForeignKey(UC, on_delete=models.CASCADE,default=None)
   fk_salle      = models.ForeignKey(Salle,on_delete=models.CASCADE)
   def get_absolute_url(self):
      return reverse("seance-detail", kwargs={"id_seance": self.id_seance})

class Groupe(models.Model):
   id_groupe = models.IntegerField(primary_key=True)
   libelle  = models.CharField(max_length=100)    
   niveau   = models.CharField(max_length=2, choices=level_uni) 
   def __str__(self):
      return self.libelle
   def get_absolute_url(self):
      return reverse("groupe-detail", kwargs={"id_groupe": self.id_groupe})
   
class Formation(models.Model): 
   id_formation     = models.IntegerField(primary_key=True)
   nom_formation    = models.CharField(max_length=100)
   ufr_rattachement = models.CharField(max_length=100,default='SEGMI') 
   def __str__(self):
      return self.nom_formation
   def get_absolute_url(self):
      return reverse("formation-detail", kwargs={"id_formation": self.id_formation})

