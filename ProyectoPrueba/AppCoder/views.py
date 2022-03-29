from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso
from .models import Curso

# Create your views here.
def curso(request, nombre, camada):

    mi_curso = Curso(nombre = nombre, camada = camada)
    mi_curso.save()
    

    
    return HttpResponse(f'Se genero el curso de {mi_curso.nombre} con la camada {mi_curso.camada}')
    