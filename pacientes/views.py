import requests
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

API_HISTORIES_URL = "http://10.128.0.6:8000"

def obtener_historiasClinicas(request):
    response = requests.get(f'{API_HISTORIES_URL}/historias')
    return JsonResponse(response.json(), safe=False)

def obtener_historiaClinica(request, history_id):
    response = requests.get(f'{API_HISTORIES_URL}/historia/{history_id}')
    return JsonResponse(response.json(), safe=False)

