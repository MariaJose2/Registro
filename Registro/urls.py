from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [     
	url(r'^$','Registro.views.inicio'),
	url(r'^crearALumno/$','Registro.views.crearAlumno'),
	url(r'^crearMateria/$','Registro.views.crearMateria'),
	url(r'^eliminarAlumno/$','Registro.views.eliminarAlumno'),
	url(r'^eliminarMateria/$','Registro.views.eliminarMateria'),
	url(r'^modificarAlumno/$','Registro.views.modificarAlumno'),
	url(r'^modificarMateria/$','Registro.views.modificarMateria'),
]
