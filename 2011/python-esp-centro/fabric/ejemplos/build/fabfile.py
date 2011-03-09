from fabric.api import local

def build():
    local("gcc -o holamundo holamundo.c")
