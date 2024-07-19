# formulario_app/views.py

from django.shortcuts import render, redirect
from .forms import FormularioForm
from django.shortcuts import render
from .models import Formulario
def formulario_view(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FormularioForm()
    return render(request, 'formulario_app/formulario.html', {'form': form})

def success_view(request):
    return render(request, 'formulario_app/success.html')



def listar_formularios_view(request):
    formularios = Formulario.objects.all()
    return render(request, 'formulario_app/listar_formularios.html', {'formularios': formularios})
