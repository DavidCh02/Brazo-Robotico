from django.shortcuts import render
from .models import Residue, SistemaRecoleccion

def index(request):
    residues = Residue.objects.all()
    return render(request, 'index.html', {'residues': residues})

def register_residue(request):
    if request.method == 'POST':
        # Lógica para registrar un residuo
        residue_type = request.POST.get('type')
        residue_weight = request.POST.get('weight')
        residue = Residue.objects.create(type=residue_type, weight=residue_weight)
        sistema = SistemaRecoleccion.objects.first()
        if sistema:
            sistema.registrar_residuo(residue)
        return render(request, 'register_residue.html', {'success': True})
    return render(request, 'register_residue.html')
