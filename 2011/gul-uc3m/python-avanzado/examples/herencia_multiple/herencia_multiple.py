class Base1:
    def metodo(self):
        print "Metodo en Base1"

class Base2:
    def metodo(self):
        print "Metodo en Base2"

class Base3:
    def metodo(self):
        print "Metodo en Base3"

class ClaseDerivada(Base1, Base2, Base3):
    pass

ins = ClaseDerivada()
ins.metodo()

