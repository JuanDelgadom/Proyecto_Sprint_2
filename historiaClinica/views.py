import requests
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def obtener_historiasClinicas(request):
    response = requests.get('http://localhost:8000/historias')
    return JsonResponse(response.json(), safe=False)

def obtener_historiaClinica(request, paciente_id):
    response = requests.get(f'http://localhost:8000/historia/{paciente_id}')
    return JsonResponse(response.json(), safe=False)
