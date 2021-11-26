from datetime import datetime

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from form import UserLogin, UserRegister
from consulta.models import Consulta
from medico.models import Medico

def login(request):
    form = UserLogin(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("cpf")
            senha = form.cleaned_data.get("senha")
            user = auth.authenticate(request, username=username, password=senha)
            if user:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, "Usuário ou senha inválidos")
                return render(request, "paciente/login.html", {'form': form})
        else:
            messages.add_message(request, messages.ERROR, "Erro ao logar", {'form': form})
    else:
        return render(request, "paciente/login.html", {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('index')

def cadastrar(request):
    form = UserRegister(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
            nome = form.cleaned_data.get("nome")
            email = form.cleaned_data.get("email")
            cpf = form.cleaned_data.get("cpf")
            telefone = form.cleaned_data.get("telefone")
            senha1 = form.cleaned_data.get("senha")
            senha2 = form.cleaned_data.get("senha2")

            if senha1 != senha2:
                messages.add_message(request,messages.WARNING, 'Senhas não conferem!')
                return render(request, "paciente/cadastro.html", {'form': form})

            if not email or not nome or not senha1 or not senha2:
                messages.add_message(request, messages.WARNING, 'Todos os campos são obrigatórios')
                return render(request, 'paciente/cadastro.html', {'form': form})

            try:
                validate_email(email)
            except:
                messages.add_message(request, messages.WARNING, 'email inválido')
                return render(request, 'paciente/cadastro.html', {'form': form})

            if User.objects.filter(email=email).exists():
               messages.add_message(request, messages.WARNING, 'E-mail já existente. Experimente fazer login')
               return render(request, 'paciente/cadastro.html', {'form': form})

            user = User.objects.create_user(
                username=cpf,
                email=email,
                first_name=nome,
                password=senha1,
            )
            messages.add_message(request, messages.SUCCESS, 'Cadastrado com sucesso')
            user.save()
            return redirect('login')
        else:
            messages.add_message(request, messages.WARNING, 'Erro ao cadastrar', {'form': form})
    else:
        return render(request, 'paciente/cadastro.html', {'form': form})

def buscar_medico(request):
    x = request.GET['buscar']

    if x is None or not x:
        messages.add_message(request,messages.INFO, 'Digite um valor valido')
        redirect('dash')
        
    medicos = Medico.objects.order_by('nome').filter(
        nome__icontains=x,
    )
    if not medicos:
        messages.add_message(request,messages.WARNING, 'Nenhum resultado encontrado')
        redirect('index')
    return render(request,'home/index.html',{'medicos':medicos})

def buscar_consulta(request):
    x = request.GET['buscar'] 
    print(dir(request))
    if x is None or not x:
        messages.add_message(request,messages.INFO, 'Digite um valor valido')
        redirect('dash')
        
    consultas = Consulta.objects.order_by('medico').filter(
        medico__nome__icontains=x,
    )
    if not consultas:
        messages.add_message(request,messages.WARNING, 'Nenhum resultado encontrado')
        redirect('index')
    return render(request,'paciente/dashboard.html',{'consultas':consultas})

def dashboard(request):
    consultas = Consulta.objects.filter(paciente=request.user.first_name).order_by('data')
    return render(request, 'paciente/dashboard.html', {'consultas': consultas})