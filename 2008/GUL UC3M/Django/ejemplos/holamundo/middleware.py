from django.http import HttpResponse

class HolaMundo:
	def process_request(self,request):
		if request.path=="/index/":
			return HttpResponse("Parando antes de procesar la consulta")

	def process_view(self,request,view_func,view_args,view_kwargs):
		if request.path=="/index2/":
			return HttpResponse("Parando antes de procesar la vista")

	def process_response(self,request, response):
		if request.path=="/holamundo/":
			return HttpResponse("Parando antes de devolver la respuesta")
		else:
			return HttpResponse(response)

	def process_exception(self,request, exception):
		return HttpResponse("Parando al procesar una excepcion")
