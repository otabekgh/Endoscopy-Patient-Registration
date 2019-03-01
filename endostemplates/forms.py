# Import forms
from django import forms

from .models import Device

class DeviceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Device
        fields = ['name']