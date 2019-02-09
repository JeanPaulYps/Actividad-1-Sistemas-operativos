import os
def crearEnlaceSimbolico (archivo1, archivo2):
    try:
        os.symlink(archivo1,archivo2)
        print("\nEnlace creado \n")
    except OSError:
        print("\nERROR \n")
        

def crearEnlaceFisico (archivo1, archivo2):
    try:
        os.link(archivo1,archivo2)
        print("\nEnlace creado \n")
    except OSError:
        print("\nERROR \n")

def cambiarPermisos (archivo,codigo):
    try:
        os.chmod(archivo,int(codigo,8))
        print("\nPermisos cambiados\n")
    except OSError:
        print("ERROR\n")

def crearProceso ():
    nuevoProceso = os.fork()
    if nuevoProceso == 0:
        os._exit(0)
    else:
        pids = (os.getpid(), nuevoProceso)
        print("\npadre:", pids[0])
    print("nuevo hijo:",nuevoProceso)
    return nuevoProceso

def matarProceso (pid):
    os.waitpid(pid,0)
       