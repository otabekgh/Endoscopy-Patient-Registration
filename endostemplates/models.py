from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Anesthesia(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class TemplateDiagnosis(models.Model):
    title       = models.CharField(max_length=255, blank=False)
    diagnosis   = models.TextField(blank=False)
    def __str__(self):
        return self.title