from django.urls import path
from . import views

app_name = 'endostemplates'
urlpatterns = [
    path('device', views.DeviceView.as_view(), name='device_page'),
    path('device/new', views.DeviceCreate.as_view(), name='device_new'),
    path('device/update/<int:pk>', views.DeviceUpdate.as_view(), name='device_update'),
    path('device/delete/<int:pk>', views.DeviceDelete.as_view(), name='device_delete'),

    path('anesthesia', views.AnesthesiaView.as_view(), name='anesthesia_page'),
    path('anesthesia/new', views.AnesthesiaCreate.as_view(), name='anesthesia_new'),
    path('anesthesia/update/<int:pk>', views.AnesthesiaUpdate.as_view(), name='anesthesia_update'),
    path('anesthesia/delete/<int:pk>', views.AnesthesiaDelete.as_view(), name='anesthesia_delete'),

    path('diagnosistemplate', views.TemplateDiagnosisView.as_view(), name='diagnosistemplate_page'),
    path('diagnosistemplate/new', views.TemplateDiagnosisCreate.as_view(), name='diagnosistemplate_new'),
    path('diagnosistemplate/update/<int:pk>', views.TemplateDiagnosisUpdate.as_view(), name='diagnosistemplate_update'),
    path('diagnosistemplate/delete/<int:pk>', views.TemplateDiagnosisDelete.as_view(), name='diagnosistemplate_delete'),
]