from GestionEDT.forms import SeanceAdminForm, OccurrenceSeanceForm
from django.contrib import admin
from schedule.admin import *
from GestionEDT.models import Seance, SeanceOccurence, SeanceCalendrier


# Register your models here.

@admin.register(SeanceCalendrier)
class SeanceCalendrierAdmin(CalendarAdmin):
    pass


@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": [
                    'timecode_debut', 'timecode_fin', 'fk_professeur', 'fk_groupe', 'fk_uc', 'fk_salle', 'calendrier'
                ]
            },
        ),
    )
    form = SeanceAdminForm


@admin.register(SeanceOccurence)
class OccurenceSeanceAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": [
                    'seance', 'debut', 'fin', 'original_start', 'original_end'
                ]
            },
        ),
    )
    form = OccurrenceSeanceForm
