from rest_framework import serializers
from Registro.models import Alumno, Materia

class AlumnoSerializable(serializers.ModelSerializer):
	class Meta:
		model = Alumno
		fields = ("Nombres","Apellidos","Cedula","Correo","Telefono","Direccion")

class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model = Materia
		fields = ("Codigo","Nombre","Creditos","Cupos","EstuMatriculados") 