import os, mensajes
def crearEnlaceSimbolico (archivo1, archivo2):
    try:
        os.symlink(archivo1,archivo2)
        print("\nEnlace creado \n")
    except OSError:
        print("\nERROR archivo no encontrado \n")
        

def crearEnlaceFisico (archivo1, archivo2):
    try:
        os.link(archivo1,archivo2)
        print("\nEnlace creado \n")
    except OSError:
        print("\nERROR archivo no encontrado \n")

def cambiarPermisos (archivo,codigo):
    try:
        os.chmod(archivo,int(codigo,8))
        print("\nPermisos cambiados\n")
    except OSError:
        print("ERROR archivo no encontrado\n")

def crearProcesos():
    entrada = 0
    while entrada != 3:
        print("PID: {}, PPID: {}".format(os.getpid(), os.getppid()))
        entrada = int(input("Oprima:\n\t1.Para crear procesos padres\n\t2.Para crear procesos hijos\n\t3.Para retroceder o terminar proceso padre\n\nOpcion: "))
        if entrada == 1:
            crearProcesosPadres()
        elif entrada == 2:
            crearProcesosHijos()
        elif entrada == 3: 
            pass

def crearProcesosPadres():
    pid = os.fork()
    if pid == 0:
        print("Proceso Creado")
        crearProcesos()
        print("Proceso padre ha terminado")
        os._exit(0)
    else:
        os.wait()

def crearProcesosHijos():
    pid = os.fork()
    if pid == 0:
        os._exit(0)
    else:
        print("PID: {}, PPID: {}".format(pid, os.getppid()))
        input("El proceso se terminara despues del mensaje, presione par continuar ")
        print("Proceso", pid,"ha terminado")
        os.wait()
       