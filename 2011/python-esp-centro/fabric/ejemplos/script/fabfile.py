from fabric.contrib.files import append
from fabric.contrib.console import confirm

def add_alias(alias,destino):
    if confirm("Esta seguro de que desea crear el alias: ("+alias+": "+destino+") ?"):
        append(alias+": "+destino, "/etc/aliases", True)
