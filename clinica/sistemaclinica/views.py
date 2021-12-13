from django.shortcuts import render, redirect
from django.http import HttpResponse
from. models import Citas, Empleados, Inventario, Jornadas, Medicamentos, Paciente, Recetas
from.forms import citaform, empleadoform, invetarioform, jornadaform, medicamentoform, pacienteform, recetaform
from django.db.models import Q
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def principal(request):
    return render(request, 'paginas/principal.html')

def registros(request):
    queryset = request.GET.get("buscar")
    registros = Paciente.objects.all()
    if queryset:
        registros = Paciente.objects.filter(
         Q(idPaciente__icontains = queryset) |
         Q(nombre__icontains = queryset)|
         Q(direccion__icontains = queryset) |
         Q(edad__icontains = queryset) |
         Q(dui__icontains = queryset)|
         Q(telefono__icontains = queryset) 
        ).distinct()
    return render(request, 'registros/index.html',{'registros': registros})

def crearpaciente(request):
    formulario = pacienteform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect(registros)
    return render(request, 'registros/crear.html',{'formulario': formulario})

def editarpaciente(request,idPaciente):
    registros = Paciente.objects.get(idPaciente=idPaciente)
    formulario= pacienteform(request.POST or None, instance=registros)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('registros')
    return render(request, 'registros/editar.html',{'formulario': formulario} )

def eliminarpaciente(request,idPaciente):
    registros = Paciente.objects.get(idPaciente=idPaciente)
    registros.delete()
    return redirect('registros')

def recetas(request):
    queryset = request.GET.get("buscar")
    recetas = Recetas.objects.all()
    if queryset:
        recetas = Recetas.objects.filter(
         Q(nombre__icontains = queryset) |
         Q(enfermedad__icontains = queryset)|
         Q(idR__icontains = queryset) |
         Q(sexo__icontains = queryset) |
         Q(medicamento__icontains = queryset)|
         Q(nombreD__icontains = queryset) |
         Q(fecha__icontains = queryset) |
         Q(sexo__icontains = queryset) 
        ).distinct()
    return render(request, 'recetas/indexR.html',{'recetas': recetas})

def crearreceta(request):
    formulario1 = recetaform(request.POST or None, request.FILES or None)
    if formulario1.is_valid():
        formulario1.save()
        return redirect(recetas)
    return render(request, 'recetas/crearR.html',{'formulario1': formulario1})

def editarrecetas(request,idR):
    recetas = Recetas.objects.get(idR=idR)
    formulario1= recetaform(request.POST or None, instance=recetas)
    if formulario1.is_valid() and request.POST:
        formulario1.save()
        return redirect('recetas')
    return render(request, 'recetas/editarR.html',{'formulario1': formulario1} )

def eliminarreceta(request,idR):
    recetas = Recetas.objects.get(idR=idR)
    recetas.delete()
    return redirect('recetas')

def inventarios(request):
    queryset = request.GET.get("buscar")
    inventarios = Inventario.objects.all()
    if queryset:
        inventarios = Inventario.objects.filter(
         Q(idI__icontains = queryset) |
         Q(equipo__icontains = queryset)|
         Q(costo__icontains = queryset) |
         Q(vidautil__icontains = queryset) |
         Q(vidameses__icontains = queryset)|
         Q(cantidad__icontains = queryset) 
        ).distinct()
    return render(request, 'inventarios/indexi.html',{'inventarios': inventarios})

def crearinventarios(request):
    formulario2 = invetarioform(request.POST or None, request.FILES or None)
    if formulario2.is_valid():
        formulario2.save()
        return redirect(inventarios)
    return render(request, 'inventarios/creari.html',{'formulario2': formulario2})

def editarinventarios(request,idI):
    inventarios= Inventario.objects.get(idI=idI)
    formulario2= invetarioform(request.POST or None, instance=inventarios)
    if formulario2.is_valid() and request.POST:
        formulario2.save()
        return redirect('inventarios')
    return render(request, 'inventarios/editari.html',{'formulario2': formulario2} )

def eliminarinventarios(request,idI):
    inventarios = Inventario.objects.get(idI=idI)
    inventarios.delete()
    return redirect('inventarios')

def citas(request):
    queryset = request.GET.get("buscar")
    citas = Citas.objects.all()
    if queryset:
        citas = Citas.objects.filter(
         Q(idC__icontains = queryset) |
         Q(nombre__icontains = queryset)|
         Q(fechac__icontains = queryset) |
         Q(hora__icontains = queryset) |
         Q(motivo__icontains = queryset)|
         Q(telefono__icontains = queryset) 
        ).distinct()
    return render(request, 'citas/indexc.html',{'citas': citas})

def crearcitas(request):
    formulario3 = citaform(request.POST or None, request.FILES or None)
    if formulario3.is_valid():
        formulario3.save()
        return redirect(citas)
    return render(request, 'citas/crearc.html',{'formulario3': formulario3})

def editarcitas(request,idC):
    citas = Citas.objects.get(idC=idC)
    formulario3= citaform(request.POST or None, instance=citas)
    if formulario3.is_valid() and request.POST:
        formulario3.save()
        return redirect('citas')
    return render(request, 'citas/editarc.html',{'formulario3': formulario3} )

def eliminarcitas(request,idC):
    citas = Citas.objects.get(idC=idC)
    citas.delete()
    return redirect('citas')

def empleados(request):
    queryset = request.GET.get("buscar")
    empleados = Empleados.objects.all()
    if queryset:
        empleados = Empleados.objects.filter(
         Q(idE__icontains = queryset) |
         Q(nombree__icontains = queryset)|
         Q(cargo__icontains = queryset) |
         Q(sexoe__icontains = queryset) |
         Q(direccione__icontains = queryset) 
        ).distinct()
    return render(request, 'empleados/indexe.html',{'empleados': empleados})

def crearempleados(request):
    formulario5 = empleadoform(request.POST or None, request.FILES or None)
    if formulario5.is_valid():
        formulario5.save()
        return redirect(citas)
    return render(request, 'empleados/creare.html',{'formulario5': formulario5})

def editarempleados(request,idE):
    empleados = Empleados.objects.get(idE=idE)
    formulario5= empleadoform(request.POST or None, instance=empleados)
    if formulario5.is_valid() and request.POST:
        formulario5.save()
        return redirect('empleados')
    return render(request, 'empleados/editare.html',{'formulario5': formulario5} )

def eliminarempleados(request,idE):
    empleados = Empleados.objects.get(idE=idE)
    empleados.delete()
    return redirect('empleados')

def medicamentos(request):
    queryset = request.GET.get("buscar")
    medicamentos = Medicamentos.objects.all()
    if queryset:
        medicamentos = Medicamentos.objects.filter(
         Q(idM__icontains = queryset) |
         Q(nombreem__icontains = queryset)|
         Q(presentacion__icontains = queryset) |
         Q(cantidad__icontains = queryset) |
         Q(viaadministracion__icontains = queryset)
        ).distinct()
    return render(request, 'medicamentos/indexm.html',{'medicamentos': medicamentos})

def crearmedicamentos(request):
    formulario6 = medicamentoform(request.POST or None, request.FILES or None)
    if formulario6.is_valid():
        formulario6.save()
        return redirect(medicamentos)
    return render(request, 'medicamentos/crearm.html',{'formulario6': formulario6})

def editarmedicamentos(request,idM):
    medicamentos = Medicamentos.objects.get(idM=idM)
    formulario6= medicamentoform(request.POST or None, instance=medicamentos)
    if formulario6.is_valid() and request.POST:
        formulario6.save()
        return redirect('medicamentos')
    return render(request, 'medicamentos/editarm.html',{'formulario6': formulario6})


def eliminarmedicamento(request,idM):
    medicamentos = Medicamentos.objects.get(idM=idM)
    medicamentos.delete()
    return redirect('medicamentos')

def jornadas(request):
    queryset = request.GET.get("buscar")
    jornadas = Jornadas.objects.all()
    if queryset:
        jornadas = Jornadas.objects.filter(
         Q(idJ__icontains = queryset) |
         Q(nombrej__icontains = queryset)|
         Q(cargoj__icontains = queryset) |
         Q(fechaj__icontains = queryset) |
         Q(horaen__icontains = queryset)|
         Q(horasa__icontains = queryset) |
         Q(horasex__icontains = queryset) 
        ).distinct()
    return render(request, 'jornadas/indexj.html',{'jornadas': jornadas})

def crearjornadas(request):
    formulario7 = jornadaform(request.POST or None, request.FILES or None)
    if formulario7.is_valid():
        formulario7.save()
        return redirect('jornadas')
    return render(request, 'jornadas/crearj.html',{'formulario7': formulario7})

def editarjornadas(request,idJ):
    jornadas = Jornadas.objects.get(idJ=idJ)
    formulario7= jornadaform(request.POST or None, instance=jornadas)
    if formulario7.is_valid() and request.POST:
        formulario7.save()
        return redirect('jornadas')
    return render(request, 'jornadas/editarj.html',{'formulario7': formulario7})

def eliminarjornadas(request,idJ):
    jornadas = Jornadas.objects.get(idJ=idJ)
    jornadas.delete()
    return redirect('jornadas')