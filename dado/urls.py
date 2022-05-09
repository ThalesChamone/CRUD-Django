from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('paciente/paciente', views.paciente, name='paciente'),
    path('paciente/paciente_add', views.adicionar_paciente, name='paciente_add'),
    path('paciente/paciente_edit/<int:paciente_pk>', views.editar_paciente, name='paciente_edit'),
    path('paciente/paciente/delete/<int:paciente_pk>', views.deletar_paciente, name='deletar_paciente'),


    path('convenio/convenio', views.convenio, name='convenio'),
    path('convenio/convenio_add', views.adicionar_convenio, name='convenio_add'),
    path('convenio/convenio_edit/<int:convenio_pk>', views.editar_convenio, name='convenio_edit'),
    path('convenio/delete/<int:convenio_pk>', views.deletar_convenio, name='deletar_convenio'),

    path('especialidade/especialidade', views.especialidade, name= 'especialidade'),
    path('especialidade/especialidade_add', views.adicionar_especialidade, name='especialidade_add'),
    path('especialidade/especialidade_edit/<int:especialidade_pk>', views.editar_especialidade, name = 'especialidade_edit'),
    path('especialidade/delete/<int:especialidade_pk>', views.deletar_especialidade, name='deletar_especialidade'),

    path('medico/medico', views.medico, name='medico'),
    path('medico/medico_add', views.adicionar_medico, name= 'medico_add'),
    path('medico/medico_edit/<int:medico_pk>', views.editar_medico, name="medico_edit"),
    path('medico/delete/<int:medico_pk>', views.deletar_medico, name="deletar_medico")
]