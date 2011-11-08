all: hellocython.so

hellocython.c: hellocython.pyx
	cython hellocython.pyx

hellocython.so: hellocython.c
	gcc -fPIC -c -I/usr/include/python2.7 hellocython.c -lpython2.7 -lm -o hellocython.o
	gcc -shared hellocython.o -o hellocython.so

clean:
	rm -f hellocython.so hellocython.o hellocython.c
