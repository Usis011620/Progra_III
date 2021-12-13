from django import forms
from django.forms import fields
from.models import Citas, Empleados, Inventario, Jornadas, Medicamentos, Paciente, Recetas

class pacienteform(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class recetaform(forms.ModelForm):
    class Meta:
        model = Recetas
        fields = '__all__'

class invetarioform(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = '__all__'

class citaform(forms.ModelForm):
    class Meta:
        model = Citas
        fields = '__all__'

class empleadoform(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'

class medicamentoform(forms.ModelForm):
    class Meta:
        model = Medicamentos
        fields = '__all__'

class jornadaform(forms.ModelForm):
    class Meta:
        model = Jornadas
        fields = '__all__'