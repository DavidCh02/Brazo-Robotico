from django.shortcuts import render
from django.http import HttpResponse
import requests

ESP32_CAM_IP = "192.168.4.1"  # IP estática configurada

def index(request):
    return render(request, 'index.html')

def move_servo(request):
    servo = request.GET.get('servo')
    angle = request.GET.get('angle')
    if servo and angle:
        angle = max(0, min(180, int(angle)))
        url = f"http://{ESP32_CAM_IP}/move?servo={servo}&angle={angle}"
        response = requests.get(url)
        return HttpResponse(response.text)
    return HttpResponse("Invalid parameters", status=400)

def stream_video(request):
    return HttpResponse(f"<img src='http://{ESP32_CAM_IP}:81/stream' width='320' height='240' alt='Video Stream'>")
