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

def crearProcesos(lista):
    entrada = 0
    while entrada != 2:
        print("La lista de procesos contiene los siguientes elementos:",lista,"\n")
        print(mensajeProcesos["FormatoMostrarProcesos"].format(os.getpid(), os.getppid()))
        entrada = int(input(mensajeProcesos["ElegirOpciones"] ))
        if entrada == 1:
            crearProcesosHijos(lista)
        elif entrada == 2: 
            if lista:
                lista.pop()
            

def crearProcesosHijos(lista):
    pid = os.fork()
    if pid == 0:
        proceso = os.getpid()
        print(mensajeProcesos["ProcesoCreado"].format(proceso))
        lista.append(proceso)
        crearProcesos(lista)
        print(mensajeProcesos["FinProcesoHijo"].format(proceso) )
        os._exit(0)
    else:
        os.wait()


        

mensajeProcesos = {}
mensajeProcesos["ElegirOpciones"] = "Oprima:\n\t1.Para crear procesos hijos\n\
    \t2.Para retroceder o terminar proceso hijo\n\nOpcion: "
mensajeProcesos["FormatoMostrarProcesos"] = "PID: {}, PPID: {}\n"
mensajeProcesos["ProcesoCreado"] = "\nProceso {} hijo creado exitosamente\n"
mensajeProcesos["FinProcesoHijo"] = "Proceso {} hijo ha terminado\n"