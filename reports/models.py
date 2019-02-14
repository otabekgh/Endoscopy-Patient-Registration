from django.db import models
#from django.urls import reverse
# Create your models here.

class EndoscopyPatients(models.Model):
    name        = models.CharField(max_length=150, blank=False)
    date_birth  = models.DateField(default=False)
    id_number   = models.CharField(max_length=9, blank=True)
    device      = models.CharField(max_length=100)
    anesthesia  = models.CharField(max_length=250)
    diagnosis   = models.TextField(blank=False, null=True)

class Device(models.Model):
    name = models.CharField(max_length=255)

class Anesthesia(models.Model):
    name = models.CharField(max_length=255)

class TemplateDiagnosis(models.Model):
    title       = models.CharField(max_length=255, blank=False)
    diagnosis   = models.TextField(blank=False)