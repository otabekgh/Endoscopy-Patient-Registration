from django.db import models

# Create your models here.
class EndosPatient(models.Model):
    name        = models.CharField(max_length=150, blank=False)
    date_birth  = models.DateField(default=False)
    id_number   = models.CharField(max_length=9, blank=True)
    anesthesia  = models.CharField(max_length=250)
    diagnosis   = models.TextField(blank=False, null=True)
    def __str__(self):
        return self.name

class EndosImage(models.Model):
    patient = models.ForeignKey(EndosPatient, on_delete= models.CASCADE)
    description = models.TextField(blank=True, null=True)
    url = models.ImageField(upload_to='static/media/patients')