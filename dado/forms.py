from django.core.validators import RegexValidator
from django import forms
from . models import Convenio, Especialidade, Medico, Paciente


##### PACIENTE FORM #####

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente        
        exclude = ()   

        labels = {
            'nome': 'Nome',
            'data_nascimento': 'Data Nascimento',
            'cpf': 'CPF',
            'endereco': 'Endereço',
            'convenio_paciente': 'Convênio',
            'medico_paciente': 'Médico',
            'telefone': 'Telefone'
        }       


        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex:. 01/01/1990'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: xxx.xxx.xxx-xx'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),         
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }
                

##### CONVENIO FORM #####              

class ConvenioForm(forms.ModelForm):
    class Meta():
        model = Convenio
        exclude = ()

        labels = {
            'nome_convenio': 'Empresa',
            'nome_fantasia': 'Nome Fantasia',
            'cnpj': 'CNPJ',
            'telefone' : 'Telefone',
        }

        widgets = {
            'nome_convenio': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_fantasia': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XX.XXX.XXX/XXXX-XX'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }


##### ESPECIALIDADE FORM #####

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        exclude = ()

        labels = {
            'especialidade' : 'Especialidade Médica'
        }

        widgets = {
            'especialidade' : forms.TextInput(attrs={'class': 'form-control'}),
        }


##### MEDICO FORM #####

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        exclude = ()

        labels = {
            'nome': 'Nome',
            'crm': 'CRM',
            'especialidade': 'Especialidade Médica',
            'telefone': 'Telefone',
            'endereco': 'Endereço'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'crm': forms.TextInput(attrs={'class': 'form-control'}),         
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'})
        }

