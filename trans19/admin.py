from django.contrib import admin
from trans19.models import Patient, Location, Visit

# Register your models here.

admin.site.register(Patient)
admin.site.register(Location)
admin.site.register(Visit)
