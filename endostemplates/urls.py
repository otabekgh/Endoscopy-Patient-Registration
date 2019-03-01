from django.urls import path
from . import views

app_name = 'endostemplates'
urlpatterns = [
    path('device', views.IndexTemplateView.as_view(), name='device_page'),
    path('device/new', views.DeviceCreate.as_view(), name='device_new'),
    path('device/update/<int:pk>', views.DeviceUpdate.as_view(), name='device_update'),
    path('device/delete/<int:pk>', views.DeviceDelete.as_view(), name='device_delete'),
]