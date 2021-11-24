from django import forms
from django.forms.models import ModelForm

from consulta.models import Consulta

class UserLogin(forms.Form):
    cpf = forms.CharField(
      label='CPF',
      widget=forms.TextInput(
        attrs={
          'class': 'input'
        }
      )
    )
    senha = forms.CharField(
      widget=forms.PasswordInput(
        attrs={
          'class': 'input'
        }
      )
    )


class UserRegister(forms.Form):
    nome = forms.CharField(
      label='Usuário',
      widget=forms.TextInput(
        attrs={
          'class': 'input'
        }
      )
    )
    cpf = forms.CharField(
      label='CPF',
      widget=forms.TextInput(
        attrs={
          'class': 'input'
        }
      )
    )
    email = forms.CharField(
      widget=forms.EmailInput(
        attrs={
          'class': 'input'
        }
      )
    )
    telefone = forms.CharField(
      label='Telefone',
      widget=forms.TextInput(
        attrs={
          'class': 'input'
        }
      )
    )
    senha = forms.CharField(
      widget=forms.PasswordInput(
        attrs={
          'class': 'input'
        }
      )
    )
    senha2 = forms.CharField(
      label='Confirme sua senha senha',
      widget=forms.PasswordInput(
        attrs={
          'class': 'input'
        }
      )
    )
                 
class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['data', 'hora']
        widgets = {
            'data': forms.DateTimeInput(attrs={'class': 'input', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'input', 'type': 'time'}),
        }

# class ConsultaForm(forms.Form):
#     data = forms.DateField(
#       label='Data',
#       widget=forms.DateInput(
#         attrs={
#           'class': 'input'
#         }
#       )
#     )
#     hora = forms.TimeField(
#       label='Hora',
#       widget=forms.TimeInput(
#         attrs={
#           'class': 'input'
#         }
#       )
#     )
#     paciente = forms.CharField(
#       label='Paciente',
#       widget=forms.TextInput(
#         attrs={
#           'class': 'input'
#         }
#       )
#     )
#     medico = forms.CharField(
#       label='Médico',
#       widget=forms.TextInput(
#         attrs={
#           'class': 'input'
#         }
#       )
#     )
