from django.contrib import admin
from .models import Device, Anesthesia, TemplateDiagnosis
# Register your models here.

admin.site.register(Device)
admin.site.register(Anesthesia)
admin.site.register(TemplateDiagnosis)
