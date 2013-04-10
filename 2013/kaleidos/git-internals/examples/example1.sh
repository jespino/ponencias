#!/bin/bash

git init repo; cd repo
echo "Version 1" > fichero.txt; git add fichero.txt
git commit -m "Version 1"
echo ""
echo "LIST OF OBJECTS"
ls .git/objects/*/* | cat
echo ""
echo "COMMIT CREATED"
git cat-file -p HEAD
echo ""
echo "TREE CREATED"
git cat-file -p b7c0dba424af1e98a3570f8125476126129e5c32
echo ""
echo "BLOB CREATED"
git cat-file -p fb8247c7b27ae4cad9e7e3e66ba95126658ea7c2
echo ""
echo "BLOB UNCOMPRESSED"
cat .git/objects/fb/8247c7b27ae4cad9e7e3e66ba95126658ea7c2 | zlib-flate -uncompress
