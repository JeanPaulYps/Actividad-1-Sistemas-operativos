class menu ():

    #Opciones es una lista que contiene otros menus
    def __init__ (self, mensaje,numeroOpciones, opciones, descripcion):
        self.mensaje = mensaje
        self.numeroOpciones = numeroOpciones
        self.opciones = opciones
        self.descripcion = descripcion

    def obtenerMensaje (self):
        return self.mensaje

    def obtenerEntrada (self):
        entrada = int(input())
        while (entrada > self.numeroOpciones or entrada <= 0):
            entrada = int(input())
        return entrada

    def obtenerOpciones (self):
        return self.opciones

    def obtenerDescripcion (self):
        return self.descripcion


    