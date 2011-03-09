from fabric.contrib.files import append

def add_alias(alias,destino):
    #append("/etc/aliases", alias+": "+destino, True)
    append(alias+": "+destino, "/etc/aliases", True)
