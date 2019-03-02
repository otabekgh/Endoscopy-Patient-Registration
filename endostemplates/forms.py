# Import forms
from django import forms

from .models import Device, Anesthesia, TemplateDiagnosis

class DeviceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Device
        fields = ['name']

class AnesthesiaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AnesthesiaForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Anesthesia
        fields = ['name']

class TemplateDiagnosisForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TemplateDiagnosisForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['diagnosis'].widget.attrs = {
            'class': 'form-control',
            'rows': '12'
        }

    class Meta:
        model = TemplateDiagnosis
        fields = ['title', 'diagnosis']