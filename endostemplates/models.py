from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=255)

class Anesthesia(models.Model):
    name = models.CharField(max_length=255)

class TemplateDiagnosis(models.Model):
    title       = models.CharField(max_length=255, blank=False)
    diagnosis   = models.TextField(blank=False)