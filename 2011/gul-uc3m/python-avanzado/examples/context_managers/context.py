from contextlib import closing

with closing(file('fichero.txt','r')) as fichero:
    for line in fichero:
        print line

class MyManager():
    def __enter__(self):
        print "Entrando en el contexto"

    def __exit__(self, *args):
        print "Saliendo del contexto"

with MyManager():
    print "Dentro del contexto"

