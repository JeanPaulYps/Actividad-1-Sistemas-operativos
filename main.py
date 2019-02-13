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
menuEnlace = menu(mensajes["NotaProcesos"] +  mensajes["elegirOpciones"], 
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
    archivo = str(input(mensajes["NotaPermisos"] + mensajes["rutaArchivoPermisos"]))
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
    funcionalidades.crearProcesos([])

        

if __name__ == "__main__": 
    controladorMenuPrincipal()