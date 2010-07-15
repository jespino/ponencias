from django.http import HttpResponse
from django.shortcuts import render_to_response
from Cheetah.Template import Template
import os
# Create your views here.

def holamundo(request):
	return HttpResponse("Hola Mundo")	

def holapersona(request,nombre):
	hola = "Hola "+nombre
	return HttpResponse(hola)

def holapersonaplantilla(request,nombre):
	return render_to_response('holamundo/hola.html',{'nombre':nombre})

def holapersonacheetah(request,nombre):
	lista = {'nombre':nombre}
	template_file_name = os.path.join(os.path.dirname(__file__),'..','templates','holamundo','holamundocheetah.tmpl')
	template_file = file(template_file_name,"r")
	t = Template(template_file.read(),searchList=[lista])
	return HttpResponse(str(t))

def fallo(request):
	algo = 0/0
