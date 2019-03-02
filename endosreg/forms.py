from django import forms
from .models import EndosPatient, EndosImage

class PatientRegForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PatientRegForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control'
        }

        self.fields['date_birth'].widget.attrs = {
            'class': 'form-control',
        }

        self.fields['id_number'].widget.attrs = {
            'class': 'form-control'
        }

        self.fields['anesthesia'].widget.attrs = {
            'class': 'form-control'
        }

        self.fields['diagnosis'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = EndosPatient
        fields = [
            'name',
            'date_birth',
            'id_number',
            'anesthesia',
            'diagnosis'
        ]