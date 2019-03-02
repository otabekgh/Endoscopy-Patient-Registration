#from django.shortcuts import render
from django.views import generic
from .models import EndosPatient, EndosImage
from django.urls import reverse_lazy
from endosreg.forms import PatientRegForm
# Create your views here.

class PatientList(generic.ListView):
    template_name = 'patient_list.html'
    model = EndosPatient
    paginate_by = 10
    def get_queryset(self):
        return EndosPatient.objects.all()

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