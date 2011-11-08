def generador():
    for x in range(1,10):
        yield x

class Iterador(object):
    def __iter__(self):
        for x in range(1,10):
            yield x

class Iterador2(object):
    def __init__(self):
        self.max = 10
        self.counter = 0

    def __iter__(self):
        return self

    def next(self):
        self.counter += 1
        if self.counter<self.max:
            return self.counter
        else:
            raise StopIteration

print "GENERADOR"
for x in generador():
    print x

print "ITERADOR"
for x in Iterador():
    print x

print "ITERADOR2"
for x in Iterador2():
    print x
