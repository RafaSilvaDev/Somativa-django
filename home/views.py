import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from consulta.models import Consulta
from form import ConsultaForm
from medico.models import Medico

from django.core.mail import send_mail

# Create your views here.
def index(request):
    dados = Medico.objects.all().order_by('nome')
    form = ConsultaForm()
    return render(request, 'home/index.html', {'form': form, 'dados': dados})

def agendar(request, xid):
    dados = Medico.objects.all().order_by('nome')
    form = ConsultaForm(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
            user = request.user.first_name
            data = form.cleaned_data.get("data")
            hora = form.cleaned_data.get("hora")
            desc = form.cleaned_data.get("descricao")
            medico = Medico.objects.get(id=xid)
            paciente = user
            email = User.objects.get(email=request.user.email)
            
            consulta = Consulta(data=data, hora=hora, descricao=desc, medico=medico, paciente=paciente)
            consulta.save()

            # send_email_consulta(email, data, hora, medico)
            
            messages.success(request, "Consulta agendada com sucesso!")
            return redirect('index')
        else:
            messages.error(request, "Erro ao agendar consulta!")
            return render(request, 'home/index.html', {'form': form, 'dados': dados})
    else:
        return render(request, 'home/index.html', {'dados': dados, 'form': form})

def buscar(request):
    x = request.GET['buscar'] 

    if x is None or not x:
        messages.add_message(request,messages.INFO, 'Digite um valor valido')
        redirect('index')
        
    dados = Medico.objects.order_by('nome').filter(
        nome__icontains = x
    )
    return render(request,'home/index.html',{'dados':dados})

def send_email_consulta(email, data, hora, medico):
    host = 'smtp.gmail.com'
    port = '587'
    login = 'rafasilvadev@gmail.com'
    senha = ''
    reciever = email

    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(login, senha)

    # cpnstruindo email tipo MIME
    corpo = f"""\
        <div style="display: flex; align-items: center; justify-content: center; background-color: brown;">
            <h1 style="color: #fff; padding: 10px;">🚨⚠ ATENÇÃO ATENÇÃO ⚠🚨</h1>
        </div>
        <br />
        <h2>Você possui uma consulta agendada no hospital Chiara Luce</h2>
        <h4>Vá até o hospital para a realização de sua consulta!</h4>
        <br />
        <hr>
        <style="padding: 15px;">
            <p>{data}</p>
            <p>{hora}</p>
            <p>{medico}</p>
        </div>
        <hr>
        <p>Obrigado por confiar em nosso trabalho! 🤝🤝</p>
    """

    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = login
    msg['Subject'] = 'ESTE EMAIL É MUITO IMPORTANTE'
    msg.attach(MIMEText(corpo, 'html'))

    server.sendmail(login, reciever, msg.as_string())