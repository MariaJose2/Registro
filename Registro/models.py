from __future__ import unicode_literals
from django.db import models

class Alumno(models.Model):
	Nombres = models.CharField(max_length=30)
	Apellidos = models.CharField(max_length=30)
	Cedula = models.CharField(max_length=10)
	Correo = models.EmailField(max_length=30,blank=True,null=True)
	Telefono = models.CharField(max_length=15,blank=True,null=True)
	Direccion = models.TextField(max_length=10,default="direccion")

	def __str__(self):
		return str(self.Cedula)

class Materia(models.Model):
	Codigo=models.IntegerField(max_length=10)
	Nombre=models.CharField(max_length=60)
	Creditos=models.IntegerField(max_length=5)
	Cupos=models.IntegerField(max_length=3)
	EstuMatriculados=models.IntegerField(max_length=3)

	def __str__(self):
		return str(self.Codigo) 
# Create your models here.
