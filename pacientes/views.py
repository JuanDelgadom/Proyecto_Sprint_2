import requests
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def obtener_historiasClinicas(request):
    response = requests.get('http://192.168.3.54:8000/historias')
    return JsonResponse(response.json(), safe=False)

def obtener_historiaClinica(request, history_id):
    response = requests.get(f'http://192.168.3.54:8000/historia/{history_id}')
    return JsonResponse(response.json(), safe=False)

