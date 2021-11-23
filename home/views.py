from django.contrib import messages
from django.shortcuts import render
from form import ConsultaForm
from medico.models import Medico

# Create your views here.
def index(request):
    dados = Medico.objects.all().order_by('nome')
    form = ConsultaForm(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
            data = form.cleaned_data.get("data")
            hora = form.cleaned_data.get("hora")
            doutor = form.cleaned_data.get("doutor")
            paciente = form.cleaned_data.get("paciente")
        else:
            messages.add_message(request, messages.ERROR, "Erro ao agendar consulta", {'form': form})
    else:
        return render(request, "paciente/login.html", {'form': form})
    return render(request, 'home/index.html', {'dados': dados})