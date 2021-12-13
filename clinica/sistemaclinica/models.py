from django.db import models
# Create your models here.

class Paciente(models.Model):
    idPaciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    edad = models.CharField(max_length=10, verbose_name='Edad')
    dui = models.CharField(max_length=15, verbose_name='Dui')
    telefono = models.CharField(max_length=10, verbose_name='Telefono')

    def __str__(self):
        fila = "Nombre:" + self.nombre + "-" + "Direccion:" + self.direccion + "-" + "Edad:" + self.edad + "-" + "Dui:" + self.dui + "-" + "Telefono:" + self.telefono
        return fila 

class Recetas(models.Model):
    idR = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre Paciente')
    fecha = models.CharField(max_length=10, verbose_name='fecha')
    edad = models.CharField(max_length=10, verbose_name='Edad')
    nombreD = models.CharField(max_length=100, verbose_name='Nombre Doctor')
    sexo = models.CharField(max_length=10, verbose_name='Sexo')
    enfermedad = models.CharField(max_length=200, verbose_name='Enfermedad')
    medicamento = models.CharField(max_length=100, verbose_name='Medicamento')

    def __str__(self):
        fila1 = "Nombre:" + self.nombre + "-" + "-" + "Edad:" + self.edad + "-" + "Nombre Doctor:" + self.nombreD + "-" + "Sexo:" + self.sexo + "-" + "Enfermedad:" + self.enfermedad + "-" + "Medicamento:" + self.medicamento
        return fila1 

class Inventario(models.Model):
    idI = models.AutoField(primary_key=True)
    equipo = models.CharField(max_length=100, verbose_name='Equipo')
    costo = models.CharField(max_length=10, verbose_name='Costo')
    vidautil = models.CharField(max_length=10, verbose_name='Vida util en Años')
    vidameses = models.CharField(max_length=100, verbose_name='Vida util en Meses')
    cantidad = models.CharField(max_length=10, verbose_name='Cantidad')
    
    def __str__(self):
        fila2 = "Equipo:" + self.equipo + "-" + "Costo:" + self.costo + "-" + "Vida Util año:" + self.vidautil + "-" + "Vida Util Meses:" + self.vidameses + "-" + "Cantidad:" + self.cantidad 
        return fila2
         
class Citas(models.Model):
    idC = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    fechac = models.CharField(max_length=30, verbose_name='Fecha')
    hora = models.CharField(max_length=10, verbose_name='Hora')
    motivo = models.CharField(max_length=100, verbose_name='Motivo de consulta')
    telefono = models.CharField(max_length=10, verbose_name='Telefono')

class Empleados(models.Model):
    idE = models.AutoField(primary_key=True)
    nombree= models.CharField(max_length=100, verbose_name='Nombre')
    cargo = models.CharField(max_length=30, verbose_name='Cargo')
    sexoe = models.CharField(max_length=10, verbose_name='Sexo')
    direccione = models.CharField(max_length=100, verbose_name='Direccion')
    
class Medicamentos(models.Model):
    idM = models.AutoField(primary_key=True)
    nombreem= models.CharField(max_length=100, verbose_name='Nombre del medicamento')
    presentacion = models.CharField(max_length=30, verbose_name='Presentacion')
    cantidad = models.CharField(max_length=10, verbose_name='Cantidad')
    viaadministracion = models.CharField(max_length=100, verbose_name='Via de administracion')
    
class Jornadas(models.Model):
    idJ = models.AutoField(primary_key=True)
    nombrej= models.CharField(max_length=100, verbose_name='Nombre')
    cargoj = models.CharField(max_length=30, verbose_name='Cargo')
    fechaj = models.CharField(max_length=10, verbose_name='Fecha')
    horaen = models.CharField(max_length=10, verbose_name='Hora de entrada')
    horasa = models.CharField(max_length=10, verbose_name='Hora de salida')
    horasex = models.CharField(max_length=10, verbose_name='Horas extras')