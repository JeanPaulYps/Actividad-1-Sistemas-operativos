import os
from menu import menu
from navegador import navegador
from mensajes import mensajes
from descripciones import descripcion

menuSalir = menu("", [], descripcion["terminar"])
menuVolver = menu("", [], descripcion["volver"])

menuCrearEnlaceSimbolico = menu("", [], descripcion["menuCrearEnlaceSimbolico"])
menuCrearEnlaceFisico = menu("", [], descripcion["crearEnlaceFisico"])
menuEnlace = menu(mensajes["elegirOpciones"], 
                    [menuCrearEnlaceSimbolico,menuCrearEnlaceFisico,menuVolver],
                    descripcion["menuEnlace"] )


menuPermisos = menu(mensajes["menuPermisos"], [menuVolver], descripcion["menuPermisos"])


menuProcesos = menu(mensajes["elegirOpciones"], [menuVolver], descripcion["menuProcesos"])


menuPrincipal = menu(mensajes["menuPrincipal"] +  mensajes["elegirOpciones"], 
                    [menuEnlace,menuPermisos,menuProcesos,menuSalir],"")


def controladorMenuPrincipal ():
    opcion = 0
    while (opcion != 4):
        opcion = menuPrincipal.obtenerEntrada()
        if (opcion == 1):
            controladorMenuEnlace()
        elif (opcion == 2):
            controladorMenuPermisos()
        elif (opcion == 3):
            controladorMenuProcesos()
        elif (opcion == 4):
            pass

def crearEnlaceSimbolico (archivo1, archivo2):
    try:
        os.symlink(archivo1,archivo2)
        print("\nEnlace creado \n")
    except OSError:
        print("\nERROR \n")
        controladorMenuPrincipal()

def crearEnlaceFisico (archivo1, archivo2):
    try:
        os.link(archivo1,archivo2)
        print("\nEnlace creado \n")
    except OSError:
        print("\nERROR \n")
        controladorMenuPrincipal()

def controladorMenuEnlace ():
    opcion = menuEnlace.obtenerEntrada()
    if (opcion == 1):
        archivo1 = str(input("Introduce la ruta del archivo: "))
        archivo2 = str(input("Introduce la ruta en donde quieres crear el enlace: "))
        crearEnlaceSimbolico(archivo1,archivo2)
    elif opcion == 2:
        archivo1 = str(input("Introduce la ruta del archivo: "))
        archivo2 = str(input("Introduce la ruta en donde quieres crear el enlace: "))
        crearEnlaceFisico(archivo1,archivo2)
    elif opcion == 3:
        pass

def controladorMenuPermisos():
    archivo = str(input("Introduce la ruta del archivo: "))
    permisos = pedirPermisos()
    cambiarPermisos(archivo, permisos)

def pedirPermisos ():
    tiposDeUsurios = ["otros", "grupo", "usuario"]
    resultado = ""
    for entrada in tiposDeUsurios:
        try:
            permiso = int( input(mensajes["mensajePermisos"].format(entrada) + "Opcion: ") )
            while permiso < 0 or permiso > 7:
                permiso = int( input(mensajes["mensajePermisos"].format(entrada) + "Opcion: " ) )
            resultado += str(permiso)
        except ValueError:
            controladorMenuPrincipal()
    return "0o" + resultado
    


def controladorMenuProcesos():
    crearProceso()


 
def cambiarPermisos (archivo,codigo):
    try:
        os.chmod(archivo,int(codigo,8))
        print("Permisos cambiados")
    except OSError:
        print("ERROR")

def crearProceso ():
    while True:
        nuevoProceso = os.fork()
        if nuevoProceso == 0:
            os._exit(0)
        else:
            pids = (os.getpid(), nuevoProceso)
            print("padre:", pids[0], "hijo:", pids[1])
        print("nuevo hijo",nuevoProceso)
        eleccion = int(input("1.Para un nuevo hijo\n2.Para salir\n"))
        if eleccion != 1:
            break



if __name__ == "__main__": 
    controladorMenuPrincipal()


