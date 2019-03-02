#from django.shortcuts import render
from django.views import generic
from .models import Device, Anesthesia, TemplateDiagnosis
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from endostemplates.forms import DeviceForm, AnesthesiaForm, TemplateDiagnosisForm
# Create your views here.

class DeviceView(generic.ListView):
    template_name = 'device_list.html'
    model = Device
    paginate_by = 10
    def get_queryset(self):
        return Device.objects.all()

class DeviceCreate(CreateView):
    template_name = 'endostemplates/templates/device_form.html'
    model = Device
    form_class = DeviceForm
    success_url = '../device'

class DeviceUpdate(UpdateView):
    template_name = 'endostemplates/templates/device_form.html'
    model = Device
    form_class = DeviceForm
    success_url = '../../device'

class DeviceDelete(DeleteView):
    template_name = 'device_delete.html'
    model = Device
    success_url = '../../device'


class AnesthesiaView(generic.ListView):
    template_name = 'anesthesia_list.html'
    paginate_by = 10
    def get_queryset(self):
        return Anesthesia.objects.all()

class AnesthesiaCreate(CreateView):
    template_name = 'endostemplates/templates/anesthesia_form.html'
    model = Anesthesia
    form_class = AnesthesiaForm
    success_url = '../anesthesia'

class AnesthesiaUpdate(UpdateView):
    template_name = 'endostemplates/templates/anesthesia_form.html'
    model = Anesthesia
    form_class = AnesthesiaForm
    success_url = '../../anesthesia'

class AnesthesiaDelete(DeleteView):
    template_name = 'anesthesia_delete.html'
    model = Anesthesia
    success_url = '../../anesthesia'


class TemplateDiagnosisView(generic.ListView):
    template_name = 'diagnosis_list.html'
    paginate_by = 5
    def get_queryset(self):
        return TemplateDiagnosis.objects.all()

class TemplateDiagnosisCreate(CreateView):
    template_name = 'endostemplates/templates/diagnosis_form.html'
    model = TemplateDiagnosis
    form_class = TemplateDiagnosisForm
    success_url = '../templatediagnosis'

class TemplateDiagnosisUpdate(UpdateView):
    template_name = 'endostemplates/templates/diagnosis_form.html'
    model = TemplateDiagnosis
    form_class = TemplateDiagnosisForm
    success_url = '../../templatediagnosis'

class TemplateDiagnosisDelete(DeleteView):
    template_name = 'diagnosis_delete.html'
    model = TemplateDiagnosis
    success_url = '../../templatediagnosis'