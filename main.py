import os,signal
from menu import menu
from navegador import navegador
from mensajes import mensajes
from descripciones import descripcion
from multiprocessing import Process,Queue
import funcionalidades


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


def controladorMenuEnlace ():
    opcion = menuEnlace.obtenerEntrada()
    if (opcion == 1):
        archivo1 = str(input(mensajes["rutaArchivoOrigen"]))
        archivo2 = str(input(mensajes["rutaArchivoDestino"]))
        funcionalidades.crearEnlaceSimbolico(archivo1,archivo2)
    elif opcion == 2:
        archivo1 = str(input(mensajes["rutaArchivoOrigen"]))
        archivo2 = str(input(mensajes["rutaArchivoDestino"]))
        funcionalidades.crearEnlaceFisico(archivo1,archivo2)
    elif opcion == 3:
        pass

def controladorMenuPermisos():
    archivo = str(input(mensajes["rutaArchivoPermisos"]))
    permisos = pedirPermisos()
    funcionalidades.cambiarPermisos(archivo, permisos)

def pedirPermisos ():
    tiposDeUsuarios = ["otros", "grupo", "usuario"]
    resultado = ""
    for tiposDeUsuario in tiposDeUsuarios:
        permiso = -1
        while permiso < 0 or permiso > 7:
            try:
                permiso = int(input(mensajes["mensajePermisos"].format(tiposDeUsuario) + "Opcion: " ) )
            except ValueError:
                print("ERROR")
        resultado += str(permiso)
    return "0o" + resultado

def controladorMenuProcesos():
    procesos = []
    eleccion = 0
    while eleccion != 4:
        eleccion = int(input(mensajes["eleccionProcesos"]))
        if eleccion == 1:
            p = funcionalidades.crearProceso()
            procesos.append(p)
            print(mensajes["procesosExistentes"], procesos,"\n\n")
        elif eleccion == 2:
            if procesos:
                p = procesos.pop()
                print(mensajes["IDProceso"], p)
                print(mensajes["procesosExistentes"], procesos,"\n\n")
                funcionalidades.matarProceso(p)
            else:
                print(mensajes["ErrorDeListaVacia"])
        else:
            print()
            break
            

        

if __name__ == "__main__": 
    controladorMenuPrincipal()