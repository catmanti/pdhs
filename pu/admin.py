from django.contrib import admin
from .models import DSDivision, MOHDivision, Institution
from data.models import Population

admin.site.register(DSDivision)
admin.site.register(MOHDivision)
# change the header of the admin panel.
admin.site.site_header = "Planning Unit Administration"


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "ds_division")


@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    list_display = ("ds_division", "year", "population")
