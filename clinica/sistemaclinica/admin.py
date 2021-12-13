from django.contrib import admin
from.models import Citas, Empleados, Inventario, Jornadas, Medicamentos, Paciente, Recetas
# Register your models here.
admin.site.register(Paciente)
admin.site.register(Recetas)
admin.site.register(Inventario)
admin.site.register(Citas)
admin.site.register(Empleados)
admin.site.register(Medicamentos)
admin.site.register(Jornadas)