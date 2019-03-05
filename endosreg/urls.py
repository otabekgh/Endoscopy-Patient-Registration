from django.urls import path
from . import views

app_name = 'endosreg'

urlpatterns = [
    path('patient', views.PatientList.as_view(), name='patient_page'),
    path('patient/new', views.PatientCreate.as_view(), name='patient_new'),
    path('patient/view/<int:pk>', views.PatientView.as_view(), name='patient_view'),
    path('patient/update/<int:pk>', views.PatientUpdate.as_view(), name='patient_update'),
    path('patient/delete/<int:pk>', views.PatientDelete.as_view(), name='patient_delete'),

    path('patient/image/<int:pk>', views.ImageList.as_view(), name='image_page'),
    path('patient/image/new', views.ImageCreate.as_view(), name='image_new'),
    path('patient/image/delete/<int:pk>', views.ImageDelete.as_view(), name='image_delete'),
]