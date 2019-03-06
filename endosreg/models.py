from django.db import models
from django.utils.timezone import now
from endostemplates.models import Anesthesia

# Create your models here.
class EndosPatient(models.Model):
    name        = models.CharField(max_length=150, blank=False)
    date_birth  = models.DateField(default='1990-12-20')
    id_number   = models.CharField(max_length=9, blank=True)
    #anesthesia  = models.CharField(max_length=250)
    anesthesia  = models.ForeignKey(Anesthesia, on_delete=models.PROTECT)
    diagnosis   = models.TextField(blank=False, null=True)
    diagnosis_date = models.DateTimeField(default=now, editable=False)
    def __str__(self):
        return self.name

class EndosImage(models.Model):
    patient = models.ForeignKey(EndosPatient, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    url = models.ImageField(upload_to='static/patients')