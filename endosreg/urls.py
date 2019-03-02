from django.urls import path
from . import views

app_name = 'endosreg'

urlpatterns = [
    path('patient', views.PatientList.as_view(), name='patient_page'),
    path('patient/new', views.PatientCreate.as_view(), name='patient_new'),
    path('patient/view/<int:pk>', views.PatientView.as_view(), name='patient_view'),
    path('patient/update/<int:pk>', views.PatientUpdate.as_view(), name='patient_update'),
    path('patient/delete/<int:pk>', views.PatientDelete.as_view(), name='patient_delete'),
]
