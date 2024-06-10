# control/urls.py
from django.urls import path
from .views import ControlLightAPIView

urlpatterns = [
    path('command/', ControlLightAPIView.as_view(), name='control_light'),
]
