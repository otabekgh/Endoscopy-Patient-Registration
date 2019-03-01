from django.urls import path
from .views import (
    IndexTemplateView,
)

app_name = 'endostemplates'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name='templates')
]