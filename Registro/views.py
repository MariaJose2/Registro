from django.shortcuts import render,redirect 

from django.contrib import messages
from django.http import HttpResponse

from .forms import FormularioAlumno, FormularioMateria
from .models import Alumno, Materia
# Create your views here.

def inicio(request):
	alumno=Alumno.objects.all()
	materia=Materia.objects.all()
	context={
		'alumno':alumno,
		'materia':materia,
	}

	return render(request,'inicio.html', context)


def crearAlumno(request):
	f = FormularioAlumno(request.POST or None)
	context ={
		"form":f,
	}

	if f.is_valid():
		datos_form = f.cleaned_data
		nombres = datos_form.get("Nombres")
		apellidos = datos_form.get("Apellidos")
		cedula = datos_form.get("Cedula")
		correo = datos_form.get("Correo")
		telefono = datos_form.get("Telefono")
		direccion = datos_form.get("Direccion")

	return render(request,'crearAlumno.html',context)

def crearMateria(request):
	f = FormularioMateria(request.POST or None)
	context ={
		"form":f,
	}

	if f.is_valid():
		datos_form = f.cleaned_data
		codigo=datos_form.get("Codigo")
		nombre = datos_form.get("Nombre")
		creditos = datos_form.get("Creditos")
		cupos = datos_form.get("Cupos")
		estuMatriculados = datos_form.get("EstuMatriculados")

	return render(request,'crearMateria.html',context)

def modificarAlumno(request):
	alumno = Alumno.objects.get(Cedula=request.GET['Cedula'])

	f = FormularioAlumno(request.POST or None)
	context={
		'alumno':alumno,
		'form':f,
   	} 
	
	f.fields["Nombres"].initial = alumno.Nombres
	f.fields["Apellidos"].initial = alumno.Apellidos
	f.fields["Correo"].initial = alumno.Correo
	f.fields["Telefono"].initial = alumno.Telefono
	f.fields["Direccion"].initial = alumno.Direccion

	if request.method == 'POST':
		if f.is_valid():
			f_data = f.cleaned_data
			alumno.Nombres = f_data.get("Nombres")
			alumno.Apellidos = f_data.get("Apellidos")
			alumno.Correo  = f_data.get("Correo")
			alumno.Telefono = f_data.get("Telefono")
			alumno.Direccion = f_data.get("Direccion")
	
			if (alumno.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado el alumno", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado el alumno", fail_silently=True)
			return redirect(inicio)

	return render(request,'modificarAlumno.html',context)

def modificarMateria(request):
	materia = Materia.objects.get(Codigo=request.GET['Codigo'])

	f = FormularioMateria(request.POST or None)
	context={
		'materia':materia,
		'form':f,
   	} 
	
	f.fields["Nombre"].initial = materia.Nombre
	f.fields["Creditos"].initial = materia.Creditos
	f.fields["Cupos"].initial = materia.Cupos
	f.fields["EstuMatriculados"].initial=materia.EstuMatriculados

	if request.method == 'POST':
		if f.is_valid():
			f_data = f.cleaned_data
			materia.Nombre = f_data.get("Nombre")
			materia.Creditos = f_data.get("Creditos")
			materia.Cupos  = f_data.get("Cupos")
			materia.EstuMatriculados = f_data.get("EstuMatriculados")

			if (materia.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado la Materia", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado la Materia", fail_silently=True)
			return redirect(inicio)

	return render(request,'modificarMateria.html',context)

def eliminarAlumno(request):
	alumno=Alumno.objects.get(Cedula=request.GET['Cedula'])
	context={
		'alumno':alumno,
	}
	return render(request,'eliminarAlumno.html',context)

def eliminarMateria(request):
	materia=Materia.objects.get(Codigo=request.GET['Codigo'])
	context={
		'materia':materia,
	}
	return render(request, 'eliminarMateria.html', context)
	


# Create your views here.
