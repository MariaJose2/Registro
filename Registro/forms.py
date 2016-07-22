from django import forms
from .models import Alumno, Materia

class FormularioAlumno(forms.Form):
	class Meta:
		model = Alumno
		fields = ("Nombres","Apellidos", "Cedula","Correo", "Telefono", "Direccion")

class FormularioMateria(forms.Form):
	class Meta:
		model = Materia
		fields = ("Codigo", "Nombre", "Creditos", "Cupos", "EstuMatriculados") 