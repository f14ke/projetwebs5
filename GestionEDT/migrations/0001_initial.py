# Generated by Django 3.1.2 on 2021-01-07 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('NumEtudiant', models.IntegerField(primary_key=True, serialize=False)),
                ('Prenom', models.CharField(max_length=30)),
                ('Nom', models.CharField(max_length=30)),
                ('Adressemail', models.EmailField(max_length=60)),
                ('Naiss', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('idFormation', models.IntegerField(primary_key=True, serialize=False)),
                ('NomFormation', models.CharField(max_length=100)),
                ('UFRRattachement', models.CharField(default='SEGMI', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('idGroupe', models.IntegerField(primary_key=True, serialize=False)),
                ('Libelle', models.CharField(max_length=100)),
                ('Niveau', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('NumProfesseur', models.IntegerField(primary_key=True, serialize=False)),
                ('Prenom', models.CharField(max_length=30)),
                ('Nom', models.CharField(max_length=30)),
                ('Adressemail', models.EmailField(max_length=60)),
                ('Naiss', models.DateField()),
                ('Statut', models.CharField(max_length=30)),
                ('Experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('Nom', models.IntegerField(primary_key=True, serialize=False)),
                ('Code', models.CharField(max_length=100)),
                ('Batiment', models.CharField(max_length=100)),
                ('Capacite', models.IntegerField()),
                ('NbPC', models.IntegerField()),
                ('Projecteur', models.IntegerField()),
                ('Tableaux', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UniteEnseignement',
            fields=[
                ('CodeMatiere', models.CharField(default=' ', max_length=30, primary_key=True, serialize=False)),
                ('ECTS', models.IntegerField()),
                ('Type', models.CharField(max_length=15)),
                ('Semestre', models.CharField(max_length=2)),
                ('fk_Formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionEDT.formation')),
            ],
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('idSeance', models.IntegerField(primary_key=True, serialize=False)),
                ('TimecodeDebut', models.DateTimeField()),
                ('TimecodeFIN', models.DateTimeField()),
                ('fk_Etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionEDT.etudiant')),
                ('fk_Professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionEDT.professeur')),
                ('fk_Salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionEDT.salle')),
                ('fk_UE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionEDT.uniteenseignement')),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='fk_Groupe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionEDT.groupe'),
        ),
    ]
