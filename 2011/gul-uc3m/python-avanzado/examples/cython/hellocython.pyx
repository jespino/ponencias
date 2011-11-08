from libc.math cimport sin

cdef double f(double x):
    return sin(x*x)

def hellocython(x):
    return "Hola cython %f" % (f(x))
