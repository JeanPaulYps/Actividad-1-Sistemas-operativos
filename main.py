import os
from menu import menu
from navegador import navegador
from mensajes import mensajes
from descripciones import descripcion

menuSalir = menu("", [], descripcion["terminar"])
menuVolver = menu("", [], descripcion["volver"])
menuEnlace = menu(mensajes["elegirOpciones"], [menuVolver],  descripcion["menuEnlace"] )
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

def controladorMenuPermisos():
    opcion = menuPermisos.obtenerEntrada()

def controladorMenuProcesos():
    opcion = menuProcesos.obtenerEntrada()

if __name__ == "__main__": 
    controladorMenuPrincipal()



