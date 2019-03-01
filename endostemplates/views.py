#from django.shortcuts import render
from django.views import generic
from .models import Device
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from endostemplates.forms import DeviceForm
# Create your views here.

class IndexTemplateView(generic.ListView):
    template_name = 'device_list.html'

    def get_queryset(self):
        return Device.objects.all()

class DeviceCreate(CreateView):
    template_name = 'templates_form.html'
    model = Device
    form_class = DeviceForm
    success_url = '../device'

class DeviceUpdate(UpdateView):
    template_name = 'templates_form.html'
    model = Device
    form_class = DeviceForm
    success_url = '../../device'

class DeviceDelete(DeleteView):
    template_name = 'delete_confirm.html'
    model = Device
    success_url = '../../device'