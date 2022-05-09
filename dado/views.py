from django.shortcuts import redirect, render
from dado.forms import ConvenioForm, EspecialidadeForm, MedicoForm, PacienteForm
from dado.models import Convenio, Especialidade, Medico, Paciente

# Create your views here.
def home(request):
    return render(request, 'home.html')


### VIEWS PACIENTE

def paciente(request):
    pacientes = Paciente.objects.all()
    context = {'pacientes': pacientes}
    return render(request, 'paciente/paciente.html', context)    



def adicionar_paciente(request):
    form = PacienteForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('paciente')

    context = {'form': form}
    return render(request, 'paciente/paciente_add.html', context)



def editar_paciente(request, paciente_pk):
    paciente = Paciente.objects.get(pk = paciente_pk)

    form = PacienteForm(request.POST or None, instance=paciente)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('paciente')

    context = {'form': form, 'paciente': paciente_pk}
    return render(request, 'paciente/paciente_edit.html', context)



def deletar_paciente(request, paciente_pk):
    paciente = Paciente.objects.get(pk = paciente_pk)
    paciente.delete()
    return redirect('paciente')

############################################################################################################################################################

### VIEWS CONVÊNIO ###

def convenio(request):
    convenios = Convenio.objects.all()
    context = {'convenios': convenios}
    return render(request, 'convenio/convenio.html', context)


def adicionar_convenio(request):
    form = ConvenioForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('convenio')

    context = {'form': form}
    return render(request, 'convenio/convenio_add.html', context)


def editar_convenio(request, convenio_pk):
    convenio = Convenio.objects.get(pk = convenio_pk)

    form = ConvenioForm(request.POST or None, instance= convenio)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('convenio')

    context = {'form': form, 'convenio': convenio_pk}
    return render(request, 'convenio/convenio_edit.html', context)


def deletar_convenio(request, convenio_pk):
    convenio = Convenio.objects.get(pk = convenio_pk)
    convenio.delete()
    return redirect('convenio')


############################################################################################################################################################

### VIEWS ESPECIALIDADE

def especialidade(request):
    especialidades = Especialidade.objects.all()
    context = {'especialidades': especialidades}
    return render(request, 'especialidade/especialidade.html', context) 


def adicionar_especialidade(request):
    form = EspecialidadeForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('especialidade')

    context = {'form': form}
    return render(request, 'especialidade/especialidade_add.html', context)


def editar_especialidade(request, especialidade_pk):
    especialidade = Especialidade.objects.get(pk = especialidade_pk)

    form = EspecialidadeForm(request.POST or None, instance = especialidade)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('especialidade')

    context = {'form': form, 'especialidade': especialidade_pk}
    return render(request, 'especialidade/especialidade_edit.html', context)


def deletar_especialidade(request, especialidade_pk):
    especialidade = Especialidade.objects.get(pk = especialidade_pk)
    especialidade.delete()
    return redirect('especialidade')


### VIEWS MEDICO

def medico(request):
    medicos = Medico.objects.all()
    context = {'medicos': medicos}
    return render(request, 'medico/medico.html', context) 
  

def adicionar_medico(request):
    form = MedicoForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('medico')

    context = {'form': form}
    return render(request, 'medico/medico_add.html', context)


def editar_medico(request, medico_pk):
    medicos = Medico.objects.get(pk = medico_pk)

    form = MedicoForm(request.POST or None, instance=medicos)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('medico')
    
    context = {'form': form, 'medico': medico_pk}
    return render(request, 'medico/medico_edit.html', context)



def deletar_medico(request, medico_pk):
    medico = Medico.objects.get(pk = medico_pk)
    medico.delete()
    return redirect('medico')