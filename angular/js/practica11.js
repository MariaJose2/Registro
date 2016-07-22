
var app = angular.module("app",["ngResource"]);

app.controller("controlador",function($scope,datosA,datosM){
	$scope.listaAlumnos= datosA.get();
	$scope.listaMaterias= datosM.get();


	$scope.ValidarCedula = function(cedula){
		var cedula = $scope.Cedula;

		for(var i=0 ; i< $scope.listaAlumnos.length; i++){
			if ( angular.equals(cedula, $scope.listaAlumnos[i].Cedula)) {
				window.location.href="practica.html";
			}
			else{
				mensaje="Cedula Invalida";
			}
		}	
		return mensaje;
	}

});
 //Definir el factori que retorne datos del webservice
 app.factory("datosA",['$resource',function($resource){
 	return $resource('http://127.0.0.1:8000/regMatAlum/Alumno/',{},{get:{method:'GET',pararms:{}, isArray:true}});
 	}
 ])
 
 app.factory("datosM",['$resource',function($resource){
 	return $resource('http://127.0.0.1:8000/regMatAlum/Materia/',{},{get:{method:'GET',pararms:{}, isArray:true}});
 	}
 ])
 