from django.contrib import admin
from .models import EndoscopyPatients, Device, Anesthesia, TemplateDiagnosis
# # Register your models here.

admin.site.register(EndoscopyPatients)
admin.site.register(Device)
admin.site.register(Anesthesia)
admin.site.register(TemplateDiagnosis)