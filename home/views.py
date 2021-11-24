from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from consulta.models import Consulta
from form import ConsultaForm
from medico.models import Medico

# Create your views here.
def index(request):
    dados = Medico.objects.all().order_by('nome')
    form = ConsultaForm()
    return render(request, 'home/index.html', {'dados': dados, 'form': form})

def agendar(request, xid):
    dados = Medico.objects.all().order_by('nome')
    form = ConsultaForm(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
            data = form.cleaned_data.get("data")
            hora = form.cleaned_data.get("hora")
            medico = Medico.objects.get(id=xid)
            paciente = User.objects.get(username=request.user.username)
            
            consulta = Consulta(data=data, hora=hora, medico=medico, paciente=paciente)
            consulta.save()
            
            messages.success(request, "Consulta agendada com sucesso!")
            return redirect('index')
        else:
            messages.error(request, "Erro ao agendar consulta!")
            return render(request, 'home/index.html', {'form': form}, {'dados': dados})
    else:
        return render(request, 'home/index.html', {'dados': dados, 'form': form})