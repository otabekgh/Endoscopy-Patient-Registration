#from django.shortcuts import render
from django.views import generic
from .models import EndosPatient, EndosImage
from django.urls import reverse_lazy, reverse
from endosreg.forms import PatientRegForm, PatientImageForm
# Create your views here.

class PatientList(generic.ListView):
    template_name = 'patient_list.html'
    model = EndosPatient
    paginate_by = 10
    def get_queryset(self):
        return EndosPatient.objects.all().order_by("-pk")

class PatientView(generic.DetailView):
    template_name = 'patient_detail.html'
    model = EndosPatient

    def get_context_data(self, **kwargs):
        context = super(PatientView, self).get_context_data(**kwargs)
        context['patient'] = EndosPatient.objects.all()
        context['images'] = EndosImage.objects.filter(patient=self.kwargs.get('pk'))
        return context

class PatientCreate(generic.CreateView):
    template_name = 'patient_form.html'
    model = EndosPatient
    form_class = PatientRegForm
    success_url = reverse_lazy('endosreg:patient_page')

class PatientUpdate(generic.UpdateView):
    template_name = 'patient_form.html'
    model = EndosPatient
    form_class = PatientRegForm
    success_url = reverse_lazy('endosreg:patient_page')

class PatientDelete(generic.DeleteView):
    template_name = 'patient_delete.html'
    model = EndosPatient
    success_url = reverse_lazy('endosreg:patient_page')


class ImageList(generic.ListView):
    template_name = 'image_list.html'
    model = EndosImage
    def get_queryset(self):
        return EndosImage.objects.filter(patient=self.kwargs.get('pk'))

class ImageCreate(generic.CreateView):
    template_name = 'image_form.html'
    model = EndosImage
    form_class = PatientImageForm
    success_url = reverse_lazy('endosreg:patient_page')

class ImageDelete(generic.DeleteView):
    template_name = 'image_delete.html'
    model = EndosImage
    success_url = reverse_lazy('endosreg:patient_page')


class MediaList(generic.ListView):
    template_name = 'image_list.html'
    model = EndosImage
    def get_queryset(self):
        return EndosImage.objects.all()