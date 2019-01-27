import os
from menu import menu
from navegador import navegador
from mensajes import mensajes
from descripciones import descripcion

menuEnlace = menu(mensajes["elegirOpciones"], [],  descripcion["menuEnlace"] )
#menuPermisos = menu()
menuPrincipal = menu(mensajes["menuPrincipal"] +  mensajes["elegirOpciones"], 
                    [menuEnlace],"")


def controladorMenuPrincipal ():
    opcion = menuPrincipal.obtenerEntrada()
    if (opcion == 1):
        controladorMenuEnlace()

def controladorMenuEnlace ():
    opcion = menuEnlace.obtenerEntrada()

if __name__ == "__main__": 
    controladorMenuPrincipal()



