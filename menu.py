class menu ():

    #Opciones es una lista que contiene otros menus
    def __init__ (self, mensaje,opciones, descripcion):
        self.mensaje = mensaje
        self.numeroOpciones = len(opciones)
        self.opciones = opciones
        self.descripcion = descripcion

    def obtenerMensaje (self):
        return self.mensaje

    def imprimirOpciones (self):
        for indice, objeto in enumerate(self.opciones):
            print("\t" + str(indice + 1) + ".", objeto.obtenerDescripcion())
        print()
    
    def obtenerEntrada (self):
        print(self.obtenerMensaje())
        self.imprimirOpciones()

        entrada = int(input("Opcion: "))
        while (entrada <= 0 or entrada > self.numeroOpciones):
            entrada = int(input("Opcion: "))
        
        print()       
        return entrada

    def obtenerOpciones (self):
        return self.opciones

    def obtenerDescripcion (self):
        return self.descripcion
