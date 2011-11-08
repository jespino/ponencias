class Base1:
    def metodo(self):
        print "Metodo en Base1"

class Base2:
    def metodo(self):
        print "Metodo en Base2"

class Base3:
    def metodo(self):
        print "Metodo en Base3"

class Base4(object):
    def metodo(self):
        print "Metodo en Base4"

class Base5(object):
    def metodo(self):
        print "Metodo en Base5"

class Base6(Base4, Base5):
    def metodo(self):
        print "Metodo en Base6"

class ClaseDerivada(Base1, Base2, Base3):
    pass

ins = ClaseDerivada()
ins.metodo()

class ClaseDerivada2(Base5, Base4, Base6):
    pass

ins = ClaseDerivada2()
ins.metodo()
