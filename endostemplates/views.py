#from django.shortcuts import render
from django.views import generic
from .models import Device, Anesthesia, TemplateDiagnosis
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from endostemplates.forms import DeviceForm, AnesthesiaForm, TemplateDiagnosisForm
from django.urls import reverse_lazy
# Create your views here.

class DeviceView(generic.ListView):
    template_name = 'device_list.html'
    model = Device
    paginate_by = 10
    def get_queryset(self):
        return Device.objects.all().order_by("-pk")

class DeviceCreate(CreateView):
    template_name = 'endostemplates/templates/device_form.html'
    model = Device
    form_class = DeviceForm
    success_url = reverse_lazy('endostemplates:device_page')
    # success_url = '../device'

class DeviceUpdate(UpdateView):
    template_name = 'endostemplates/templates/device_form.html'
    model = Device
    form_class = DeviceForm
    success_url = reverse_lazy('endostemplates:device_page')

class DeviceDelete(DeleteView):
    template_name = 'device_delete.html'
    model = Device
    success_url = reverse_lazy('endostemplates:device_page')


class AnesthesiaView(generic.ListView):
    template_name = 'anesthesia_list.html'
    paginate_by = 10
    def get_queryset(self):
        return Anesthesia.objects.all().order_by("-pk")

class AnesthesiaCreate(CreateView):
    template_name = 'endostemplates/templates/anesthesia_form.html'
    model = Anesthesia
    form_class = AnesthesiaForm
    success_url = reverse_lazy('endostemplates:anesthesia_page')

class AnesthesiaUpdate(UpdateView):
    template_name = 'endostemplates/templates/anesthesia_form.html'
    model = Anesthesia
    form_class = AnesthesiaForm
    success_url = reverse_lazy('endostemplates:anesthesia_page')

class AnesthesiaDelete(DeleteView):
    template_name = 'anesthesia_delete.html'
    model = Anesthesia
    success_url = reverse_lazy('endostemplates:anesthesia_page')


class TemplateDiagnosisView(generic.ListView):
    template_name = 'diagnosis_list.html'
    paginate_by = 5
    def get_queryset(self):
        return TemplateDiagnosis.objects.all().order_by("-pk")

class TemplateDiagnosisCreate(CreateView):
    template_name = 'endostemplates/templates/diagnosis_form.html'
    model = TemplateDiagnosis
    form_class = TemplateDiagnosisForm
    success_url = reverse_lazy('endostemplates:diagnosistemplate_page')

class TemplateDiagnosisUpdate(UpdateView):
    template_name = 'endostemplates/templates/diagnosis_form.html'
    model = TemplateDiagnosis
    form_class = TemplateDiagnosisForm
    success_url = reverse_lazy('endostemplates:diagnosistemplate_page')

class TemplateDiagnosisDelete(DeleteView):
    template_name = 'diagnosis_delete.html'
    model = TemplateDiagnosis
    success_url = reverse_lazy('endostemplates:diagnosistemplate_page')