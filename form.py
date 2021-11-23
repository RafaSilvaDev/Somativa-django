from django import forms

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

class ConsultaForm(forms.Form):
    data = forms.DateField(
      label='Data',
      widget=forms.DateInput(
        attrs={
          'class': 'input'
        }
      )
    )
    hora = forms.ChoiceField(
      label='Hora',
      widget=forms.TimeInput(
        attrs={
          'class': 'input'
        }
      )
    )
    paciente = forms.CharField(
      label='Paciente',
      widget=forms.TextInput(
        attrs={
          'class': 'input'
        }
      )
    )
    medico = forms.CharField(
      label='Médico',
      widget=forms.TextInput(
        attrs={
          'class': 'input'
        }
      )
    )