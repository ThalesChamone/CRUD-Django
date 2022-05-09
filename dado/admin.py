from django.contrib import admin
from dado.models import Convenio, Especialidade, Medico, Paciente

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Convenio)
admin.site.register(Especialidade)
admin.site.register(Medico)