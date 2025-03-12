from django.urls import path
from . import views

urlpatterns = [
    path('historiasClinicas/', views.obtener_historiasClinicas, name='obtener_historiasClinicas'),
    path('historiaClinica/<int:paciente_id>/', views.obtener_historiaClinica, name='obtener_historia_clinica'),
]