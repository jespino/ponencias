#!/bin/bash

hg init nombre-del-repositorio
cd nombre-del-repositorio

echo "LINEA 1" > fichero.txt
hg add fichero.txt

hg commit -m "Version inicial"

echo "LINEA 2" >> fichero.txt

hg commit -m "Añadiendo un cambio"

hg log

hg diff

echo "LINEA 3" >> fichero.txt

hg diff

hg commit -m "Añadiendo otro cambio"

hg diff -r 0
hg diff -r 1
hg diff -r 2

hg checkout -r 0
hg checkout -r 1
hg checkout -r 2

cd ..
hg clone nombre-del-repositorio miclon

cd nombre-del-repositorio

echo "LINEA 4" >> fichero.txt
hg commit -m "Añadiendo otro cambio"

cd ../miclon

hg pull
hg update

cd ../nombre-del-repositorio

echo "LINEA 5" >> fichero.txt
hg commit -m "Añadiendo otro cambio"

cd ../miclon

echo "LINEA 1" >> fichero2.txt
hg add fichero2.txt
hg commit -m "Añadiendo otro cambio"

hg pull
hg merge
hg commit -m "Merge"

cd ../nombre-del-repositorio

echo "LINEA 6" >> fichero.txt
hg commit -m "Añadiendo otro cambio"

cd ../miclon

echo "LINEA 7" >> fichero.txt
hg commit -m "Añadiendo otro cambio"

hg pull
hg merge

# Solventamos el conflicto

hg resolve -m fichero.txt
hg commit -m "Merge"
hg push

hg branch nuevarama
echo "LINEA 8" >> fichero.txt
hg commit -m "Añadiendo otro cambio"

hg branches

hg checkout default
hg merge nuevarama
hg commit -m "Mezclando la rama nuevarama a default"

echo "fichero.data" > .hgingore
