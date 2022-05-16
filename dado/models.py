from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

NAME_VALIDATOR = RegexValidator(r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$", "Formato inválido de nome")
CPF_VALIDATOR = RegexValidator(r"[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}", "CPF com formato inválido")
ENDERECO_VALIDATOR = RegexValidator(r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$", "Formato Inválido")
CNPJ_VALIDATOR = RegexValidator(r"^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$", "CNPJ com formato inválido")

# Create your models here.
class Convenio(models.Model):
    nome_convenio = models.CharField(validators = [NAME_VALIDATOR], max_length=200)
    nome_fantasia = models.CharField(max_length=200)
    cnpj = models.CharField(validators = [CNPJ_VALIDATOR], max_length=20)
    telefone = PhoneNumberField(null=False, blank=False, unique= True)

    def __str__(self) -> str:
        return self.nome_convenio
        

class Especialidade(models.Model):
    especialidade = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.especialidade


class Medico(models.Model):
    nome = models.CharField(validators= [NAME_VALIDATOR] ,max_length=170)
    crm = models.CharField(max_length=20)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    telefone = PhoneNumberField(null=False, blank=False, unique= True)
    endereco = models.CharField(validators=[ENDERECO_VALIDATOR] ,max_length=200)

    def __str__(self) -> str:
        return self.nome


class Paciente(models.Model):
    nome = models.CharField(validators = [NAME_VALIDATOR], max_length=155)
    data_nascimento = models.DateField()    
    cpf = models.CharField(validators=[CPF_VALIDATOR], max_length=14)
    endereco = models.CharField(max_length=200)
    convenio_paciente = models.ForeignKey(Convenio, blank=True, null=True, on_delete=models.DO_NOTHING)
    medico_paciente = models.ForeignKey(Medico, blank=True, null=True, on_delete=models.DO_NOTHING)
    telefone = models.CharField(max_length=15, unique=True) 

    def __str__(self) -> str:
        return self.nome







